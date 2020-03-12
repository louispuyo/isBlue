import json
import requests

url = 'http://127.0.0.1:5000'

# test data
data = {'Pclass': 3, 'Age': 2, 'SibSp': 1, 'Fare': 50}

data = json.dumps(data)
print(data)
r_survey = requests.post(url, data)
print(r_survey)
send_request = requests.post(url, data)
print(send_request)
print(send_request.json())
