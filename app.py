from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import time
import requests
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run()
