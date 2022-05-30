
## Person and Car Detection

  

This repo contains transfer learning approach for fine-tune person and car detection problem.

## Training Script:
In `train.ipynb`
 - We have used YOLOv5 to train the current model.
 - The data preprocessing includes conversion of COCO labels to YOLO txt format.
 - The training has been done on 2000 images and validated on 239 samples for 10 epochs.
 - We have used `yolov5m.pt` as our pretrained checkpoint. Alternatively, we can use higher accurate heavy checkpoints from here: [https://github.com/ultralytics/yolov5#pretrained-checkpoints](https://github.com/ultralytics/yolov5#pretrained-checkpoints)
 
 - The training has been done on `google colab`, checkout the code using colab icon below:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KananVyas/person_car_detection_yolov5/blob/master/train.ipynb)

## Accuracy Metrics

With this training, **mAP@0.5 achieved 71% accuracy** on validation set.

![alt text](https://github.com/KananVyas/person_car_detection_yolov5/blob/master/metrics/results.png?raw=true)

![alt text](https://github.com/KananVyas/person_car_detection_yolov5/blob/master/metrics/F1_curve.png?raw=true)

 - As seen above, all classes are captured with mAP@0.5=0.71 at the threshold of >0.3.
 - Hence, we can set our confidence threshold between 0.25-0.3.


