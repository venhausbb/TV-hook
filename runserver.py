import os
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Flask app running!"

# Start the server using the port provided by Render
if __name__ == "__main__":
    # Get the PORT environment variable (Render assigns this dynamically)
    port = int(os.environ.get("PORT", 5000))
    # Run the app on 0.0.0.0 so it's accessible externally
    app.run(host='0.0.0.0', port=port)
