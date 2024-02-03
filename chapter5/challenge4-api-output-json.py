#  Python code to read output of api call in json format

import requests
import json

def make_api_call(api_url):
    try:
        response = requests.get(api_url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON content of the response
            data = response.json()
            return data
        else:
            # Print an error message if the request was not successful
            print(f"API request failed with status code {response.status_code}")
            return None
    except Exception as e:
        # Handle any exceptions that may occur during the API call
        print(f"Error during API call: {e}")
        return None

# if __name__ == "__main__": Allows You to Execute Code When the File Runs as a Script,
# but Not When It’s Imported as a Module
# for most the scripts we run in this book, we could use this line
# unless we create a module and we would want to import the module
# in another script

if __name__ == "__main__":
    # Replace 'your_api_url' with the actual API URL you want to call
    api_url = 'your_api_url'
    
    api_data = make_api_call(api_url)

    if api_data:
        # Print the JSON data or perform further processing
        print("API response in JSON format:")
        print(json.dumps(api_data, indent=2))
