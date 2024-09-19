"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from Flask_TV_hook import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# Add the webhook route here
@app.route('/webhook', methods=['POST'])
def webhook():
    """Endpoint for receiving webhooks from TradingView."""
    data = request.json  # Get the JSON data sent in the webhook request
    if data:
        print(f"Received webhook data: {data}")
        return jsonify({"status": "Webhook received"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400
