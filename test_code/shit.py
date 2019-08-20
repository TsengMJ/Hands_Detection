import numpy as np
import imutils
import cv2
import os

def readimg(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    (y, cr, cb) = cv2.split(ycrcb)
    cr1 = cv2.GaussianBlur(cr, (25, 25), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 

    return skin

def getPalm(img, skin):
    cnts = cv2.findContours(skin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # (x,y),radius = cv2.minEnclosingCircle(cnts[0])
    # x = int(x)
    # y = int(y)
    # radius = int(radius)
    # print(x)
    # print(y)
    # print(radius)

    x,y,w,h=cv2.boundingRect(cnts[0])
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


    try:
        c = cnts[0]
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # draw the contour and center of the shape on the image
        cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
        cv2.circle(img, (cX, cY), 7, (255, 0, 0), -1)
        cv2.putText(img, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    except:
        pass
    # cv2.circle(img, (x, y), radius, (0, 0, 255), 2)
        
    return w, h, img

def detectNum(w, h):
    
    if w<350:
        if h<360:
            print(0)
        elif h<386:
            print(1)
        elif h<417:
            print(2)
        elif h<436:
            print(3)
        elif h<439:
            print(4)
    else:
        print(5)



## Image version
for i in range(6):
    img = cv2.imread("../test/test_{}.jpg".format(i))
    skin = readimg(img)
    (w,h,img) = getPalm(img, skin)

    detectNum(w, h)

    cv2.imshow("Img",img)
    cv2.waitKey(0)

# cv2.imshow("Skin", skin)
cv2.destroyAllWindows()


## Video version

# vcap = cv2.VideoCapture(0)
# success, _ = vcap.read()

# while success:
#     success, frame = vcap.read()
#     skin = readimg(frame)
#     (w,h,img) = getPalm(frame, skin)

#     detectNum(w, h)

#     cv2.imshow("Img",img)
#     if cv2.waitKey(20) == 27:
#         break

# cv2.destroyAllWindows()