# Hands_Detection
We Present yolo based hand tracking. 

## Preparation 
Plz make sure you are have an python3.6 environment or folllow the steps below to create one.

### Create Environment
1. Downloas Anaconda's Official Website [[Here](https://www.anaconda.com/distribution/)]
2. Install Anaconda
```
cd to/download/path
sudo chmod +x <Anaconda-installer-name>
./<Anaconda-installer-name>  ## make sure anser yes for every question
```
3. Create a python3.6 environment
```
source ~/.bashrc
conda create --name py36 python=3.6
conda activte py36
```
## Yolov3
Download yolov3 and darknet we need. See more detail [[Here](https://pjreddie.com/darknet/yolo/)]

1. If you don't already have Darknet installed, folllow [this](https://pjreddie.com/darknet/install/). Or instead of reading all that just run
```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
```











We gonna use opencv to control cameras 

---
Install uvcdynctrl
```
sudo apt install uvcdynctrl
```

Use uvcdynctrl to get your camera's resolution
```
uvcdynctrl -f
```
