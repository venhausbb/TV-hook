import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook route to handle signals
@app.route('/send_signal', methods=['POST'])
def send_signal():
    try:
        data = request.json
        if not data:
            return jsonify({"message": "No JSON data received", "status": "failed"}), 400
        
        # Extract relevant fields from the incoming webhook data
        order_type = data.get('order_type')
        price = data.get('price')
        tp = data.get('tp')  # Take Profit
        sl = data.get('sl')  # Stop Loss

        # Log the incoming data
        print(f"Received {order_type} signal - Price: {price}, Take Profit: {tp}, Stop Loss: {sl}")
        
        # Respond to the request
        return jsonify({"message": "Signal received", "status": "success"}), 200
    
    except Exception as e:
        print(f"Error processing signal: {str(e)}")
        return jsonify({"message": "Internal server error", "status": "failed"}), 500

if __name__ == '__main__':
    # Use the 'PORT' environment variable to bind to the appropriate port, defaulting to 5000 if not set
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
