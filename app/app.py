from flask import Flask, render_template, request, jsonify
import os
import requests
import json

app = Flask(__name__)

env = os.getenv('APP_ENV', 'dev')
config_filename = f"{env}_config.json"

with open(config_filename) as f:
    config_data = json.load(f)
app.config.from_mapping(config_data)

def fetch_exchange_rates():
    try:
        api_key = app.config['CURRENCYFREAKS_API_KEY']
        base_url = 'https://api.currencyfreaks.com/v2.0/rates/latest'
        params = {'apikey': api_key}
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('rates')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exchange-rate', methods=['POST'])
def get_exchange_rate():
    source_currency = request.form.get('source_currency')
    target_currency = request.form.get('target_currency')
    amount = float(request.form.get('amount'))

    exchange_rates = fetch_exchange_rates()

    if exchange_rates is None:
        return jsonify({"error": "Failed to fetch exchange rates"}), 500

    if not source_currency or not target_currency:
        return jsonify({"error": "Source and target currencies are required"}), 400

    if source_currency not in exchange_rates:
        return jsonify({"error": f"Source currency '{source_currency}' not supported"}), 404

    if target_currency not in exchange_rates:
        return jsonify({"error": f"Target currency '{target_currency}' not supported"}), 404

    source_rate = float(exchange_rates.get(source_currency))
    target_rate = float(exchange_rates.get(target_currency))

    exchange_rate = target_rate / source_rate
    
    return jsonify({
        "source_currency": source_currency,
        "target_currency": target_currency,
        "exchange_rate": exchange_rate,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)