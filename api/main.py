import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from PIL import Image
import torch
import json
import time

global model

#Model Loading
def load_model():
    weights_path = "weights/best.pt"
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path)
    return model
model = load_model()
print("LOADED MODEL")

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome from the Person and Car Detection API"}

#Prediction endpoint
@app.post("/predict")
def get_image(file: UploadFile = File(...)):
    global model
    final_json = {}
    image = Image.open(file.file)
    start = time.time()
    results = model(image, size=416)
    end = time.time()
    df = json.loads(results.pandas().xyxy[0].to_json(orient="records"))
    final_json['output'] = df
    final_json['inference_time'] = (end-start)*1000
    print(final_json)
    return final_json

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7000)