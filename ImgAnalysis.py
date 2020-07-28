import requests
import json
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

class ImgAnalysis: 
    def __init__(self):
        load_dotenv()
        self.key = os.getenv("SECRET_KEY")
        self.endpoint = os.getenv("ENDPOINT")
        self.analyzeUrl = self.endpoint + "vision/v2.0/analyze"
    
    def remoteImg(self, imgUrl):
        img = Image.open(BytesIO(requests.get(imgUrl).content))

        headers = {'Ocp-Apim-Subscription-Key': self.key}
        params = {'visualFeatures': 'Categories,Description,Color'}
        data = {'url': imgUrl}
        response = requests.post(self.analyzeUrl, headers=headers,
                         params=params, json=data)
        response.raise_for_status()
        analysis = response.json()
        imgCaption = analysis["description"]["captions"][0]["text"].capitalize()
        return imgCaption

    def localImg(self, imgPath):
        print(imgPath)
        imgData = open(imgPath, "rb").read()
        img = Image.open(BytesIO(imgData))

        headers = {'Ocp-Apim-Subscription-Key': self.key,
                'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'Categories,Description,Color'}
        response = requests.post(
            self.analyzeUrl, headers=headers, params=params, data=imgData)
        response.raise_for_status()
        analysis = response.json()
        imgCaption = analysis["description"]["captions"][0]["text"].capitalize()
        return imgCaption
    
    def test(self):
        print("hello")

