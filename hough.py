#!/usr/bin/python2.7
import cv2 as cv 
import numpy as np 
from matplotlib import pyplot as plt 

imgO = cv.imread('hough.jpg')
img = cv.cvtColor(imgO, cv.COLOR_BGR2GRAY)
print img.shape
edges = cv.Canny(img, 100, 200,apertureSize=3)
# cv.imshow('canny', edges)
# cv.waitKey(0)

lines = cv.HoughLines(edges, 1, np.pi/180, 125)
print lines 
for rho,theta in lines[0]:
    print rho,theta
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho 
    y0 = b*rho 
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*(a))
    cv.line(imgO, (x1,y1), (x2,y2), (0,0,255),5)
cv.imwrite('houghres.jpg', imgO)

