## Usaeg python3 png_to_jpg.py full/path/to/the/folder 

from PIL import Image
import os
import sys

FOLDER_PATH = sys.argv[1]
files = os.listdir(FOLDER_PATH)

for file in files:
    if file.endswith(".png"):
        name = file.split(".")[0]
        newName = "{}.jpg".format(name)
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(newName)

        ## Delete Original *.png file
        command = "rm {}/{}".format(FOLDER_PATH, file)
        os.system(command)
