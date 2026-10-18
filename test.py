import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    "data": [[0.4926315134678635, -0.4046340348298488, 0.21416799772426984, -0.6426594650965456, -0.8017438981058532, 2.853225638640355, 341.0, 2112.0, 0.0, 1408.0, 705.0]]
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Response:", response.text)