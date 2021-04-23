import cv2
import imutils
import numpy as np
import sys

print(sys.argv[1])

cv2.namedWindow('Out', cv2.WINDOW_AUTOSIZE)

def nothing(x):
    pass

cv2.createTrackbar('Value','Out',50,255,nothing)

vid = cv2.VideoCapture(sys.argv[1])


bg = cv2.imread(f"bg/{sys.argv[2]}")
print(bg)
bg = cv2.resize(bg,(720,540))

def conv(img,bg,value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower =  np.array([28, 52, value])
    upper = np.array([102, 255, 255])
    mask = cv2.inRange(gray, lower, upper)
    mask_inv = cv2.bitwise_not(mask)

    res = cv2.bitwise_and(img,img, mask= mask_inv)

    bg_res = cv2.bitwise_and(bg,bg, mask= mask)
    res = cv2.bitwise_or(bg_res,res, mask= None)
    return res

while(1):
    img = vid.read()[1]
    img = cv2.resize(img,(720,540))
    v = cv2.getTrackbarPos('Value','Out')
    res = conv(img,bg,v)
    cv2.imshow('Out',res)
    k = cv2.waitKey(50) & 0xFF
    if k == 27:
        break
