import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
