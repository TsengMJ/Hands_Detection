# Hands_Detection
We Present a yolo based real-time(GPU) hand tracking. 

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
conda install jupyter
```

### TsesorFlow-Gpu and Cuda
Make sure you follow the steps [Here](https://www.tensorflow.org/install/gpu) carefully


### OpenCV
Make sure you follow the steps [Here](https://docs.opencv.org/4.1.1/d2/de6/tutorial_py_setup_in_ubuntu.html) carefully.
Also install opencv in your environment
```
conda activate py36
conda install -c conda-forge opencv 
```


### YOLOv3
Download yolov3 and darknet we need. See more detail [[Here](https://pjreddie.com/darknet/yolo/)]

1. If you don't already have Darknet installed, folllow [this](https://pjreddie.com/darknet/install/). Or instead of reading all that just run
```
git clone https://github.com/pjreddie/darknet.git
cd darknet
vim Makefile## SET GPU=1, OPENCV=1
make
```
2. Download pretrained darknet-weight
```
wget https://pjreddie.com/media/files/darknet53.conv.74
```

## Preparing Data
Download our processed data or you can follow this [article ](https://medium.com/@manivannan_data/how-to-train-yolov2-to-detect-custom-objects-9010df784f36) to customize data


[Note]: The date format is
`
<class> <x> <y> <w> <h>
`
* class: Integer, represent the class you write in the classes.txt. 
* x: Float, represent the **center** of the object in Width. -> x = absolute_x / image_width
* y: Float, represent the object in Height. -> y = absolute_y / image_height
* w: Float, represent the object's Width. -> w = object_width / image_width
* h: Float, represent the object's Height. -> h = object_height / image_height


1. Download our data
```
cd path/to/darknet
git clone https://github.com/TsengMJ/Hands_Detection.git
cd Hands_Detection/; cp hand.data ../cfg/hand.data
cp hand-yolov3.cfg ../cfg/hand-yolov3.cfg
python Data/process.py
```
Then you will get train.txt and test.txt in Data folder

2. Setting config files
```
cd ../cfg
vim hand.data 
  ## Set train and valid to the train.txt and test.txt
  ## Set names to hand.names in Data folder
  ## Set backup to a clean folder for saving trained weight
```

More detail [Here](https://medium.com/@manivannan_data/how-to-train-yolov3-to-detect-custom-objects-ccbcafeb13d2).

## Training 
Start training 
```
cd path/to/darknet
sudo ./darknet detector train cfg/hand.data cfg/hand-yolov3.cfg darknet53.conv.74
```
Might wait for at least 1hr to cancel the training


## Testing 
Plz connect your camera first. Then
```
./darknet detector demo cfg/hand.data cfg/hand-yolov3.cfg <trained-weight>
```

## Result
![](demo/demo_1.png)
![](demo/demo_2.png)
![](demo/demo_3.gif)








