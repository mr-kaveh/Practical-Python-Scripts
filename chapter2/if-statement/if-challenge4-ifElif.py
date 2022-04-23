# Requests Library
import requests

try:
    response = requests.get("https://api.publicapis.org/entries")
    if(response.status_code == 200): # If requests response code 200(success)
        print('response code 200')
    elif(response.status_code == 404): # If requested URL not found/exist
        print('URL not found')
    else:
        print('undefined Error') # All other response codes
except requests.ConnectionError:
    print("failed to connect")