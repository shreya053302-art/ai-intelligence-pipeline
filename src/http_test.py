import requests

url = "https://httpbin.org/get"

response = requests.get(url)

print("Status code:", response.status_code)
print("Response received:", response.ok)