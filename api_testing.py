# import requests

# # URL of the API endpoint
# api_url = 'http://127.0.0.1:5000/update_car_price'  # Replace with your API URL

# # Input data to send in the request
# input_data = {
#     "model": "Cultus"  # Replace with the input you want to test
# }

# # Send a POST request to the API endpoint
# response = requests.post(api_url )

# # Print the response
# print(response)

import firebase_admin
from firebase_admin import storage, credentials
import json
cred = credentials.Certificate("subsidized-fueling-system-firebase-adminsdk-e5hzp-38a5c23549.json")

firebase_admin.initialize_app( cred, {'storageBucket': 'subsidized-fueling-system.appspot.com'})

def load_category_list():
    bucket = storage.bucket()
    
    # Download the category_list.json file from Firebase Storage
    blob = bucket.blob('category_list.json')
    json_data = blob.download_as_text()

    # Load JSON content into car_dict
    global car_dict
    car_dict = json.loads(json_data)

    print({"message": "Category list loaded successfully"})

load_category_list()
print(car_dict)