#!/usr/bin/python3

import argparse
import numpy as np 
import cv2
import math

red = (0,0,255)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

def deg2rad(deg):
	rad = deg * (math.pi / 180)
	return rad

def make_circle(radius, center_x, center_y):
	for theta in range(0, 359):
		for r in range(0, radius, 10):
			x1 = center_x + r*(math.cos(deg2rad(theta)))
			y1 = center_y + r*(math.sin(deg2rad(theta)))
			x2 = center_x + r*(math.cos(deg2rad(theta + 1)))
			y2 = center_y + r*(math.sin(deg2rad(theta + 1)))

			cv2.line(image, (int(x1),int(y1)), (int(x2),int(y2)), red, 3)

def check_yellow(x,y):
	(b,g,r) = image[x,y]
	#print("b: ", b, "g: ", g, "r: ", r)
	if b > 10 and b < 50:
		if g > 150 and g < 255:
			if r > 100 and r < 255:
				return True
	else:
		return False

#This can be used to check the color inside each circle 
def yellow_circle_check(radius, center_x, center_y):
	yellow_pixels = 0
	total_pixels = 0

	for theta in range(0, 360):
		for r in range(0, radius):
			xpixel = center_x + r*(math.cos(deg2rad(theta)))
			ypixel = center_y + r*(math.sin(deg2rad(theta)))
			total_pixels += 1
			#(b,g,r) = image[int(xpixel), int(ypixel)]
			#print("b: ", b, "g: ", g, "r: ", r)
			if check_yellow(int(xpixel), int(ypixel)) == True:
				yellow_pixels += 1
	
	percent_yellow = (yellow_pixels / total_pixels)*100
	print("Percent yellow pixels: ", percent_yellow)
	if percent_yellow > 80:
		return True
	else:
		return False

#convert image to greyscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#implement gaussian blur
blurred = cv2.GaussianBlur(gray, (7,7), 0)

#canny edge detection
canny = cv2.Canny(blurred, 30, 150)

#find the contours, count them and mark them
(cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#create copy of the image
balls = image.copy()

#draw the contours in the color image copy
cv2.drawContours(balls, cnts, -1, (255,0,0), 2)
cv2.imshow("Contours", balls)
cv2.waitKey(0)

yellow_circle_check(120, 490, 160)

make_circle(120, 490, 160)		 

cv2.imshow("image", image)
cv2.waitKey(0)
