import requests

endpoint = "http://127.0.0.1:8000/product/create/"
# endpoint = "http://127.0.0.1:8000/"


data = {
    'title': 'thsi field is done'
}


get_response = requests.post(endpoint, data=data)

print(get_response.json())
print(get_response.status_code)