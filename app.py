from flask import Flask, request, jsonify , render_template, redirect, url_for
import firebase_admin
from firebase_admin import storage, credentials
import json


app = Flask(__name__)

cred = credentials.Certificate("templates\subsidized-fueling-system-firebase-adminsdk-e5hzp-38a5c23549.json")

firebase_admin.initialize_app( cred, {'storageBucket': 'subsidized-fueling-system.appspot.com'})

@app.route('/get_car_category', methods=['GET'])
def get_car_category():
    input_data = request.args.get("model")

    if not input_data:
        return jsonify({"error": "Input not provided"}), 400

    output_data = car_dict.get(input_data, "Not found")
    response = {
        
        "category": input_data,
        "price": output_data
    }
    return jsonify(response), 200

@app.route('/', methods=['GET', 'POST'])
def update_car_category():
    load_category_list()
    if request.method == 'POST':
        Category = request.form['Category']
        Price = request.form['Price']
        car_dict[Category] = Price

        bucket = storage.bucket()
        blob = bucket.blob('category_list.json')
        blob.upload_from_string(json.dumps(car_dict))


        return redirect(url_for('update_car_category'))

    return render_template('update_car_category.html', car_dict=car_dict)


def load_category_list():
    bucket = storage.bucket()

    # Download the category_list.json file from Firebase Storage
    blob = bucket.blob('category_list.json')
    json_data = blob.download_as_text()

    # Load JSON content into car_dict
    global car_dict
    car_dict = json.loads(json_data)

    return jsonify({"message": "Category list loaded successfully"}), 200



if __name__ == '__main__':
    app.run(debug=True)
