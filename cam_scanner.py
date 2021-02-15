import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

img = cv.imread("test.jpg",1)
print(img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(gray)

med = cv.medianBlur(gray,5)

#global thresholding
ret,th1 = cv.threshold(med,127,255,cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(med,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

th3= cv.adaptiveThreshold(med,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow("image",th3)

cv.waitKey(0)

cv.destroyAllWindows()
