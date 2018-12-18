# Keras_Head_Detection_YoloV3
An implimentation of yoloV3 in head detection ,keras and tensorflow backend used

This repository is based on [qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3
).We train the keras yolov3 model in [brainwash dataset](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/software-and-datasets/),and make detection on human heads by this model.

## Dependence
Hear is my python environment,you could build your environment according to contents below selectively.

- Python                3.5
- Keras                 2.2.4
- Tensorflow            1.12.0
- opencv-contrib-python 3.4
- PIL                   5.0.0
- numpy                 1.15.2

## Quick Start

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
2. Convert the Darknet YOLO model to a Keras model.
3. Run YOLO detection.

```
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]
```

## Training
1. Generate your own annotation file and class names file.  
    One row for one image;  
    Row format: `image_file_path box1 box2 ... boxN`;  
    Box format: `x_min,y_min,x_max,y_max,class_id` (no space).  
    For VOC dataset, try `python voc_annotation.py`  
    Here is an example:
    ```
    path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
    path/to/img2.jpg 120,300,250,600,2
    ...
    ```

2.Modify train.py and start training.
    `python train.py`
    Specify your train weights, class file and anchor file by modify some lines in train.py related with these variables, or you can modify train.py and use command line to change those default settings.

## Testing
Use command below to test your images and videos.
```
yolo_video.py --image #Test images
yolo_video.py --input #Test videos

```
