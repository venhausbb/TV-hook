from flask import Flask, request, jsonify
import os  # <-- Make sure to import the os module

app = Flask(__name__)

@app.route('/send_signal', methods=['POST'])
def send_signal():
    data = request.json
    order_type = data.get('order_type')
    price = data.get('price')
    tp = data.get('tp')
    sl = data.get('sl')

    # Log received data (for testing)
    print(f"Received signal: {order_type}, Price: {price}, TP: {tp}, SL: {sl}")

    # Respond with success
    return jsonify({"status": "success", "message": "Signal received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
