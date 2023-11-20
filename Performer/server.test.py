import requests
from controlparam import ControlParam
from time import sleep


url = "http://127.0.0.1:3838"

print("GET param")
res = requests.get(url+"/param")
print(res.json())

sleep(1)

print("POST start")
res = requests.post(url+"/start")
print(res.text)

sleep(1)

print("POST param")
res = requests.post(url+"/param",json={"delta":15.0,"gamma":0.2})
print(res.text)

sleep(1)

print("GET param")
res = requests.get(url+"/param")
print(res.json())

sleep(1)

print("POST stop")
res = requests.post(url+"/stop")
print(res.text)