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


@app.route('/', methods= ['GET'])
def get_gstins():
    gstin_lst = []
    req_url = request.headers["req_url"]
    subscription_key = "f635607382d34585b32d5f3e13b4bc11"
    computervision_client = ComputerVisionClient("https://zsft-cv.cognitiveservices.azure.com/", CognitiveServicesCredentials(subscription_key))

    #headers = {'Ocp-Apim-Subscription-Key': subscription_key,'Content-Type': 'application/octet-stream',  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}
    #with open("C:\\Users\\Admin\\Pictures\\chinaaa.jpg", 'rb') as f:
    #    data = f.read()
    #initial_response = requests.post(
    #    "https://eastus.api.cognitive.microsoft.com/vision/v3.2/read/analyze", headers=headers, data=data)

    #read_operation_location = initial_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = req_url.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        final_response = computervision_client.get_read_result(operation_id)
        if final_response.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    for text_result in final_response.analyze_result.read_results:
            for line in text_result.lines:
                for word in line.words:
                    if(len(word.text) == 15):
                        #if(re.match("^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$" ,word.text)):
                        gstin_lst.append(word.text)
    return jsonify({"GSTINS" : gstin_lst})


if __name__ == '__main__':
    app.run()
