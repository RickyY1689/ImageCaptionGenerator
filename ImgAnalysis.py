import requests
import json
from PIL import Image
from io import BytesIO

class ImgAnalysis: 
    def __init__(self):
        self.key = "0d137a82e2b1446c968a1b65c5ee6f8b"
        self.endpoint = "https://centralus.api.cognitive.microsoft.com/"
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

