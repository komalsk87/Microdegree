import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)

print(type(data))  # This will print <class 'dict'> since the response is a JSON object

# payload ={"name":"Komal" , "id":1}

# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)

print(type(data))  # This will print <class 'dict'> since the response is a JSON object
