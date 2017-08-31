#!/usr/bin/python2.7

import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 

img = cv.imread('chess.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)

# img[dst>0.05*dst.max()] = [0,0,255]
ret,dst = cv.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)

ret,labels,stats,centroids = cv.connectedComponentsWithStats(dst)
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray, np.float32(centroids), (5,5), (-1,-1), criteria)
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
cv.imwrite('chesscorner.jpg', img)
cv.imshow('dst', img)
if cv.waitKey(0) & 0xff==27:
    cv.destroyAllWindow()