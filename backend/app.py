from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('house price.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return "House price prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        features = [[
            data['income'],
            data['age'],
            data['rooms'],
            data['bedrooms'],
            data['population']
        ]]

        input_data = np.array(features)

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)

        return jsonify({
            'predicted_price': float(prediction[0])
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
