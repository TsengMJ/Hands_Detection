import numpy as np
import imutils
import cv2
import os

## Return grayscale image with white pixels are skin areas
def getSkin(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    (y, cr, cb) = cv2.split(ycrcb)
    cr1 = cv2.GaussianBlur(cr, (25, 25), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 

    return skin

vcap = cv2.VideoCapture(0)
success, _ = vcap.read()

while success:
    success, frame = vcap.read()
    skin = getSkin(frame)

    cv2.imshow("Img", frame)
    cv2.imshow("Skin", skin)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()