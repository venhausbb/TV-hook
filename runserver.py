@app.route('/send_signal', methods=['POST'])
def send_signal():
    try:
        data = request.get_json()
        order_type = data['order_type']
        price = data['price']
        tp = data['tp']
        sl = data['sl']

        # For testing purposes, just print the data
        print(f"Received {order_type} order: Price={price}, TP={tp}, SL={sl}")
        
        return jsonify({"status": "success", "message": "Signal received"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
