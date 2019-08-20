import cv2
import numpy as np
import matplotlib.pyplot as plt

vcap = cv2.VideoCapture(1)
vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

success, frame = vcap.read()

while success:
    succes, frame = vcap.read()
    if success:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        left_frame = frame[ :480, :640] 
        right_frame = frame[ :480, 640:] 

        stereo = cv2.StereoBM_create(numDisparities=16, blockSize=21)
        depth_map = stereo.compute(left_frame, right_frame)

        # min = depth_map.min()
        # max = depth_map.max()
        # depth_map = np.uint8(255 * (depth_map - min) / (max - min))

        # cv2.imshow('left',left_frame)
        # cv2.imshow('right', right_frame)
        # cv2.imshow('depth', depth_map/32)
        plt.clf()
        plt.imshow(depth_map, 'gray')
        plt.show()

    if cv2.waitKey(20) == 27:
        break

vcap.release()
cv2.destroyAllWindows()