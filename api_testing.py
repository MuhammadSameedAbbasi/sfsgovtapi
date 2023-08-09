import requests

# URL of the API endpoint
api_url = 'http://127.0.0.1:5000/update_car_price'  # Replace with your API URL

# Input data to send in the request
input_data = {
    "model": "Cultus"  # Replace with the input you want to test
}

# Send a POST request to the API endpoint
response = requests.post(api_url )

# Print the response
print(response)
