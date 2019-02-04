#!/usr/bin/python3

import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# load and convert image into numpy array
image = cv2.imread(args["image"])

# come up with a way for it to test if it is a tennis ball 
# grab a region and show in cv2 window
middle = image[100:150, 100:150]

cv2.imshow("Middle", middle)
cv2.waitKey(0)
# maybe look for a bunch of yellow pixels in the middle or something
yellow_pixels = 0

main_color_middle = "white"

def check_color(x,y):
	color = "black"
	(b,g,r) = image[x,y]
	if g > 200 and r > 200 and b < 100:
		color = "yellow"
	elif g > 70 and r > 150 and b < 100:
		color = "orange"
	return color

def check_region(x1, x2, y1, y2, color):
	total_pixels = 0
	sought_color_pixels = 0

	for i in range(x1, x2):
		for j in range(y1, y2):
			total_pixels += 1
			if check_color(i,j) == color:
				sought_color_pixels += 1

	percent_sought_color = (sought_color_pixels / total_pixels)*100
	return percent_sought_color

percent_yellow = check_region(100,150,100,150, "yellow")
percent_orange = check_region(100,150,100,150, "orange")

print("Percentage of yellow pixels: ", percent_yellow, " %")
print("Percentage of orange pixels: ", percent_orange, " %")

if percent_yellow > 80:
	print("That is a tennis ball")	
elif percent_orange > 80:
	print("That is a basketball")
else:
	print("I don't know what kind of ball that is")
