#!/usr/bin/python3

import argparse
import numpy as np 
import cv2
import math

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#helper function to locate the center point of the tennis ball
def get_contour_center(c):
	M = cv2.moments(c)
	Cx = -1
	Cy = -1
	if (M['m00'] != 0):
		Cx = int(M['m10']/M['m00'])
		Cy = int(M['m01']/M['m00'])
	return Cx, Cy

#convert the image into HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hsv)
cv2.waitKey(0)

#find the upper and lower bounds of the yellow color
yellowLower = (30, 75, 75)
yellowUpper = (60, 255, 255)

#define a mask using the lower and upper bounds
mask = cv2.inRange(hsv, yellowLower, yellowUpper)

cv2.imshow("mask", mask)
cv2.waitKey(0)

(contours, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#create copy of the color image
image_copy = image.copy()

cv2.drawContours(image_copy, contours, -1, (255,0,0), 2)
cv2.imshow("Contours", image_copy)
cv2.waitKey(0)

#mark the central point of each contour
for contour in contours:
	cx, cy = get_contour_center(contour)
	cv2.circle(image_copy, (cx, cy), 3, (0,0,255), -1)

cv2.imshow("lock on targets", image_copy)
cv2.waitKey(0)
