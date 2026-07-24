from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allows your HTML file to communicate with Python

# Get the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "emails.txt")

@app.route('/save-email', methods=['POST'])
def save_email():
    # Extract the JSON data from the frontend fetch request
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({"status": "error", "message": "No email provided"}), 400

    # "a" mode opens the file and appends text to the end without deleting old content
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(email + "\n")
        
    print(f" Saved to text file: {email}")
    return jsonify({"status": "success", "message": "Email saved to website files!"})

if __name__ == '__main__':
    # Starts the local server on http://127.0.0.1:5000
    app.run(port=5000, debug=True)
