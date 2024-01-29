from flask import Flask, jsonify
import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



@app.route("/api/people-count", methods=['GET'])
def getPeopleCount():
    dosya_yolu = "C:\\Users\\enesk\\OneDrive\\Masaüstü\\Yoloprojesi\\Object-Detection-101 (1)\\peoplecounteryolov8-main\\deneme.txt"

    with open(dosya_yolu, "r") as dosya:
        dosya_icerigi = dosya.read()

    # Dosya içeriğini yazdır
    print("Dosya İçeriği:")
    print(dosya_icerigi)


    return dosya_icerigi;

if __name__ == "__main__":
    app.run(debug=True, port=9090)
