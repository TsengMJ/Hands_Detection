## Usage python3 recore_image full/path/to/a/folder newFolderName

import cv2
import sys
import os

Path = sys.argv[1]
Folder_Name = sys.argv[2]
Folder_path = os.path.join(Path, Folder_Name)

if not os.path.exists(Folder_path):
    os.mkdir(Folder_path)

vcap = cv2.VideoCapture(0)
success, frame = vcap.read()
if success:
    cv2.imshow('Camera', frame)

num = 0
while success:
    succes, frame = vcap.read()
    if success:      
        cv2.imshow('Camera', frame)

        if cv2.waitKey(10) == ord('c'):
            name = "{}/{}_{}.jpg".format(Folder_path, Folder_Name, num)
            cv2.imwrite(name, frame)
            print('Save {}'.format(name))
            num = num+1

        if cv2.waitKey(10) == 27:
            break

vcap.release()
cv2.destroyAllWindows()


