  

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

## Testing Script

 with `test.ipynb`

 - We can load the trained model from the given path.
 - Infer the model and plot the detections using the script.
 - Run this script with google colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KananVyas/person_car_detection_yolov5/blob/master/test.ipynb)

![alt text](https://github.com/KananVyas/person_car_detection_yolov5/blob/master/metrics/output.png?raw=true)
 

## Docker support and API:

Using `/api/main.py`:

 - We can run inference using FastAPI endpoint.
 - Execute `python3 /api/main.py` to run uvicorn server on port `7000`. It will automatically load the model and by calling `/predict` endpoint in Postman, we can get inference JSON as an output.
 - To run in containarized env, build the `Dockerfile`
 - - `docker build -f ./api/Dockerfile -t person_car_api  .`
 - After succesfully building the docker,
 - - `docker run -it  --net host  person_car_api`
 - After running the container, call `http://127.0.0.1:7000/predict` POST request and send image as `file` form-data to the endpoint.
 - The output json structure will look like:

```json
{"output":  [{
	"xmin":  14.2618331909,
	"ymin":  76.5265274048,
	"xmax":  380.9652099609,
	"ymax":  397.6776123047,
	"confidence":  0.8891581893,
	"class":  0,
	"name":  "person"
	}],
"inference_time":  556.9939613342285 }
```