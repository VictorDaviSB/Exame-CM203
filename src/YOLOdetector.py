from ultralytics import YOLO
import cv2
import numpy as np
import math

class object_detector():
    def __init__(self, model = YOLO('yolov8m.pt')):
        self.model = model

    def detect(self, frame):
        results = self.model(frame, stream=True)
        
        centers=[]
        for r in results:
            boxes = r.boxes
            for box in boxes:
                if(int(box.cls) == 32):
                    x1, y1, x2, y2 = box.xyxy[0]
                    centers.append(np.array([[int((x1+x2)/2)], [int((y1+y2)/2)]]))
                
        return centers
        

    

    
