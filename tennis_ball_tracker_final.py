#!/usr/bin/python3

import numpy as np 
import cv2 

def filter_color(rgb_image, lower_bound_color, upper_bound_color, show=False):
	#convert the image into the HSV color space
	hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
	if show:
		cv2.imshow("HSV Image", hsv_image)

	#define a mask using the upper and lower bounds of the yellow color
	mask = cv2.inRange(hsv_image, lower_bound_color, upper_bound_color)

	return mask

def getContours(binary_image):
	(contours, _) = cv2.findContours(binary_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	return contours

def get_contour_center(contour):
	M = cv2.moments(contour)
	cx = -1
	cy = -1
	if (M['m00']!=0):
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
	return cx, cy

def draw_ball_contour(rgb_image, contours):
	#black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3], 'uint8')

	for c in contours:
		area = cv2.contourArea(c)
		perimeter = cv2.arcLength(c, True)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		if (area > 3000):
			cv2.drawContours(rgb_image, [c], -1, (255,0,0), 2)
			#cv2.drawContours(black_image, [c], -1, (255,0,0), 1)
			cx, cy = get_contour_center(c)
			cv2.circle(rgb_image, (cx,cy), 3, (0,0,255), -1)
			#cv2.circle(black_image, (cx,cy), 3, (0,0,255), -1)
			#cv2.imshow("RGB Image Contours", rgb_image)
			#cv2.imshow("Black Image Contours", black_image)

def detect_ball_in_frame(image_frame):
	yellowLower = (30, 75, 75)
	yellowUpper = (60, 255, 255)
	binary_image_mask = filter_color(image_frame, (30, 75, 75), (60, 255, 255))
	contours = getContours(binary_image_mask)
	draw_ball_contour(image_frame, contours)
	cv2.imshow("Frame", image_frame)


#***********************************#
video_capture = cv2.VideoCapture(0)

while(True):
	ret, frame = video_capture.read()
	detect_ball_in_frame(frame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()
#***********************************#