# imports
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
import argparse
import os
import imutils 
from skimage.filters import threshold_local
from .perspective import four_point_transform

BASE_DIR = os.path.abspath('.')
LOCAL_STORAGE_PATH = os.path.join(BASE_DIR, 'samples', 'scanned'),

def scan_img(img_path):

	# reding image
	image = cv2.imread(img_path)

	# validation
	if image is None:
		return None

	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image = imutils.resize(image, height = 500)

		
	# converting the image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# applying gaussian blur
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	# finding edges using canny edge detection method
	edged = cv2.Canny(gray, 75, 200)

	# cv2.imshow('canny', edged)
	# cv2.waitKey(0)

	# finding th econtous in the image
	# cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	# # print('contours : ', cnts)

	# cnts = imutils.grab_contours(cnts)
	# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
	# cnt = 0

	# # loop over the contours
	# for c in cnts:
	# 	# finding the perimeter of the page
	# 	peri = cv2.arcLength(c, True)
	# 	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# 	# cnt = approx
	# 	if len(approx) == 4:
	# 		cnt = approx
	# 		break

	# drawing the contour of paper
	# try:
	# 	cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)

	# except:
	# 	print("[ERROR] Couldn't find document edges properly...")
	# 	return None
	
	# cv2.imshow('scanned', image)

	# applying for-point-transformation
	# warped = four_point_transform(orig, cnt.reshape(4, 2) * ratio)

	# for scanned effect
	warped = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	T = threshold_local(warped, 11, offset = 10, method = "gaussian")
	warped = (warped > T).astype("uint8") * 255

		
	# saving image to the output directory
	temp = img_path.split('/')
	str = ''
	for i in temp[0:-1]:
		str += i
	scanned_path = os.path.join(str, 'scanned.png')
	# filename = os.path.join(LOCAL_STORAGE_PATH, 'scanned.png')
	filename = 'scanned.png'
	print(os.getcwd())
	os.chdir(os.path.join(BASE_DIR, 'samples', 'scanned'))
	current_path = os.path.abspath('.')
	print(current_path)
	cv2.imwrite(filename, imutils.resize(warped, height=650))
	os.chdir(current_path)
	# print(os.getcwd())
	print('image saved')
	return imutils.resize(warped, height=650)