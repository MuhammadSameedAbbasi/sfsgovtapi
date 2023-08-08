from flask import Flask, request , jsonify

app = Flask(__name__)

car_dict = {"Cultus": "270.5",
            "Mehran": "200.5",
            "Corolla": "400.5",
            "Civic": "500.5",
            "City": "450.5"
            }


@app.route('/classify', methods=['Post'])
def classify():
    # Get the image file from the request
    #file = request.files['image']

    try:
        input_data = request.json["model"]
        output_data = car_dict.get(input_data, "Not found")
        response = {input_data: output_data}
        return jsonify(response), 200
    except KeyError:
        return jsonify({"error": "Input not provided"}), 400
    

    # TODO: Load the machine learning model and use it to classify the image
 


if __name__ == '__main__':
    app.run(debug=True)
