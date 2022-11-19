# importing requests and json
import requests, json
from datetime import datetime

# base URL
BASE_URL = "https://catfact.ninja/fact"

# HTTP request
response = requests.get(BASE_URL)

match response.status_code:
    case 200:
        print(response.json()["fact"])
    case 400:
        print("Bad request")
    case  401 | 403:
        print("not allowed")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")
