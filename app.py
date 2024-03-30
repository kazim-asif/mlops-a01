from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)

# Load the trained model
model = joblib.load('melbourne_house_price_model.pkl')


@app.route('/', methods=['GET'])
def main():
    return jsonify({'message': 'Hello from Python'})


# Define an endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    rooms = data['Rooms']
    bathroom = data['Bathroom']
    landsize = data['Landsize']
    lattitude = data['Lattitude']
    longtitude = data['Longtitude']

    # Make prediction
    prediction = model.predict([[rooms, bathroom, landsize, lattitude, longtitude]])

    return jsonify({'predicted_price': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)
