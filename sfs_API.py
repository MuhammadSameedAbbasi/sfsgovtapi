from flask import Flask, request, jsonify , render_template, redirect, url_for

app = Flask(__name__)

car_dict = {
#     "Cultus": "Small",
#     "Mehran": "Small",
#     "Corolla": "Large",
#     "Civic": "Large",
#     "City 2007": "Medium"
}

@app.route('/', methods=['GET'])
def get_car_price():

    response = {
        "car_model": 'test',
        "price": 300000
    }
    return jsonify(response), 200


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

@app.route('/update_car_price', methods=['GET', 'POST'])
def update_car_price():
    if request.method == 'POST':
        model = request.form['model']
        price = request.form['price']
        car_dict[model] = price
        return redirect(url_for('update_car_price'))

    return render_template('update_car_price.html', car_dict=car_dict)

if __name__ == '__main__':
    app.run(debug=True)
