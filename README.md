# ImageCaptionGenerator

## Purpose and Process
This python program aims to provide captions to images inputted through either an image url or by local file path. <br/>
GUI was designed using Tkinter and caption is generated using computer vision provided by Microsoft Azure's <br/>
computer vision API.

## Usage 
Note that this program requires a Microsoft Azure account <br/>
Using your Microsoft Azure account, create a cognitive service resource group and create an account your program will use to access the API <br/>
To run this program, install both python files as well as the jpg image into one folder.<br/>
Using notepad, open ImgAnalysis.py and input your Microsoft Azure computer vision account key and endpoint. <br/>

## Reasources 
Documentation on the Microsoft Azure Computer Vision API can be found [here](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/). <br/>
Creating resource groups and accounts can be done on [Azure's CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&tabs=azure-cli#run-the-azure-cli) <br/>
and the commands accepted within the CLI are available [here](https://docs.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-create)
