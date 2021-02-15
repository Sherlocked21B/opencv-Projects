import cv2 as cv 
import numpy as np 

cap = cv.VideoCapture(0)
cv.namedWindow("Tackbars")

def nothing(x):
    print(x)

cv.createTrackbar("L_H","Tackbars",0,179,nothing)
cv.createTrackbar("L_S","Tackbars",0,255,nothing)
cv.createTrackbar("L_V","Tackbars",0,255,nothing)
cv.createTrackbar("U_H","Tackbars",179,179,nothing)
cv.createTrackbar("U_S","Tackbars",255,255,nothing)
cv.createTrackbar("U_V","Tackbars",255,255,nothing)

while True:
    ret , frame = cap.read()
    
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV);

    l_h = cv.getTrackbarPos("L_H","Tackbars")
    l_s = cv.getTrackbarPos("L_S","Tackbars")
    l_v = cv.getTrackbarPos("L_V","Tackbars")
    u_h = cv.getTrackbarPos("U_H","Tackbars")
    u_s = cv.getTrackbarPos("U_S","Tackbars")
    u_v = cv.getTrackbarPos("U_V","Tackbars")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    
    edges = cv.inRange(hsv,l_b,u_b)

    result = cv.bitwise_and(frame,frame,mask=edges)

    cv.imshow("orginalImage",frame)
    cv.imshow("edges",edges)
    cv.imshow("result",result)

    key = cv.waitKey(1)

    if key == 27:
        break 

cv.destroyAllWindows()
