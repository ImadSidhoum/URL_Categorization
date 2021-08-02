import requests
import json

URLs = ['https://medium.com/nerd-for-tech/url-feature-engineering-and-classification-66c0512fb34d','https://www.kaggle.com/shawon10/url-classification-by-naive-bayes']
data = json.dumps({"signature_name": "serving_default", "data": URLs})
headers = {"content-type": "application/json"}
json_response = requests.post(f'http://127.0.0.1:5001/predict', data=data, headers=headers)
js = json_response.text 
if js:
    predictions = js
    print(predictions)