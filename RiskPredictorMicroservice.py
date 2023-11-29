from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/predict-risk', methods=['POST'])
def predict_risk():
    # Receive home parameters from Smart Home Controller Microservice
    home_parameters = request.json['parameters']
    
    # Simplified risk prediction (replace with actual logic)
    risk_level = 'low' if home_parameters['temperature'] < 25 else 'high'

    # If risk level is low, update thermostat temperature in Smart Home Controller Microservice
    if risk_level == 'low':
        update_temperature_url = 'http://52.54.211.229:5000/update-temperature'
        new_temperature = 22  # You can set the desired temperature here
        requests.post(update_temperature_url, json={'temperature': new_temperature})

    return jsonify({'risk_level': risk_level})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
