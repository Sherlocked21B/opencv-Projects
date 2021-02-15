import cv2 as cv
import numpy as np

img = cv.imread("photo.jpg",1)

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

med = cv.medianBlur(grey,5)

edges = cv.adaptiveThreshold(med,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,9)

color = cv.bilateralFilter(img,9,250,250)

cartoon = cv.bitwise_and(color,color,mask=edges)

cv.imshow("cartoon",cartoon)

cv.waitKey(0)
cv.destroyAllWindows()

