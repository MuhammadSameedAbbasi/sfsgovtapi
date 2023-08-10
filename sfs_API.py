from flask import Flask, request, jsonify , render_template, redirect, url_for
import firebase_admin
from firebase_admin import storage, credentials
import json


app = Flask(__name__)

# car_dict = {}
#     "Cultus": "Small",
#     "Mehran": "Small",
#     "Corolla": "Large",
#     "Civic": "Large",
#     "City 2007": "Medium"
# }

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

    return jsonify({"message": "Category list loaded successfully"}), 200


@app.route('/get_car_price', methods=['GET'])
def get_car_price():
    input_data = request.args.get("model")

    if not input_data:
        return jsonify({"error": "Input not provided"}), 400

    output_data = car_dict.get(input_data, "Not found")
    response = {
        "car_model": input_data,
        "price": output_data
    }
    return jsonify(response), 200

@app.route('/', methods=['GET', 'POST'])
def update_car_price():
    load_category_list()
    if request.method == 'POST':
        model = request.form['model']
        price = request.form['price']
        car_dict[model] = price
        return redirect(url_for('update_car_price'))

    return render_template('update_car_price.html', car_dict=car_dict)

if __name__ == '__main__':
    app.run(debug=True)
