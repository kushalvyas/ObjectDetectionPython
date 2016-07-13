"""
Author : Kushal Vyas

Run : python file.py <templateImage> <actualImage>

"""

import sys, cv2
import numpy as np

def main(template, actualImage):
	tImage = cv2.imread(template, 0)
	aImage = cv2.imread(actualImage)
	aCopy = aImage.copy()
	aImage = cv2.cvtColor(aImage, cv2.COLOR_BGR2GRAY)
	th, tw = tImage.shape[:2]

	match = cv2.matchTemplate(aImage, tImage, cv2.TM_SQDIFF)
	minmaxlocs = cv2.minMaxLoc(match)
	topcorner = minmaxlocs[-2]
	bottomcorner=  (topcorner[0] + tw, topcorner[1]+th)
	cv2.rectangle(aCopy, topcorner, bottomcorner, (0, 0, 255), 2)

	cv2.imshow("actual Iamge", aCopy)
	cv2.waitKey()


if __name__ == '__main__':
	args = sys.argv[1:]
	print args
	if (len(args) is not 2):
		print "Please pass cmd args for template and actual image"
		sys.exit(-1)

	main(args[0], args[1])