# Requests Library
import requests

# Free fake API for testing and prototyping.
# Powered by JSON Server + LowDB.
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if(str(response).find('200') != -1): # If requests response code 200(success)
    print('response code 200')
elif(str(response).find('404') != -1): # If requested URL not found/exist
    print('URL not found')
else:
    print('undefined Error') # All other response codes