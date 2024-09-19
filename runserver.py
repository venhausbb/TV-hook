from flask import Flask, jsonify, request
import requests
import json
import os

app = Flask(__name__)

# Your TradingView Webhook URL (replace with your actual TradingView webhook URL)
TRADINGVIEW_WEBHOOK_URL = "https://tradingview.com/api/webhook/YOUR_UNIQUE_WEBHOOK_URL"

def send_signal(order_type, price, tp, sl):
    """
    Function to send a signal to TradingView via webhook
    :param order_type: 'buy' or 'sell'
    :param price: the price of the asset
    :param tp: take profit
    :param sl: stop loss
    :return: response status code
    """
    payload = {
        "order": order_type,
        "price": price,
        "tp": tp,
        "sl": sl
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(TRADINGVIEW_WEBHOOK_URL, json=payload, headers=headers)
    
    return response.status_code, response.content

@app.route('/send_signal', methods=['POST'])
def receive_signal():
    """
    Flask route to handle incoming signal requests.
    The body of the request should contain order_type, price, tp, and sl.
    """
    data = request.json
    order_type = data.get("order_type")
    price = data.get("price")
    tp = data.get("tp")
    sl = data.get("sl")

    status_code, response_content = send_signal(order_type, price, tp, sl)

    return jsonify({
        "status_code": status_code,
        "response": response_content.decode("utf-8")
    })

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
