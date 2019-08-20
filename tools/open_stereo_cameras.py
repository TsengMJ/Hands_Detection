import cv2

vcap = cv2.VideoCapture(1)
vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

success, frame = vcap.read()
if success:
    cv2.imshow('Camera', frame)

while success:
    succes, frame = vcap.read()
    if success:
        cv2.imshow('Camera', frame)
    
    if cv2.waitKey(20) == 27:
        break

vcap.release()
cv2.destroyAllWindows()


