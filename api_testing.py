import requests

# URL of the API endpoint
api_url = 'http://localhost:5000/classify'  # Replace with your API URL

# Input data to send in the request
input_data = {
    "model": "Cultus"  # Replace with the input you want to test
}

# Send a POST request to the API endpoint
response = requests.post(api_url, json=input_data)

# Print the response
print(response.json())
