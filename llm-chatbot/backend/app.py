from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
from llm_integration import get_llm_response
import firebase_admin
from firebase_admin import credentials, firestore
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='../frontend')
CORS(app)

SYSTEM_PROMPT = "You are a helpful movie director assistant."

# Initialize Firebase and Firestore
try:
    cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_PATH"))
    firebase_admin.initialize_app(cred)
    db = firestore.client()  # Initialize Firestore
    logger.info("Firestore initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Firestore: {str(e)}")

@app.route('/')
def serve_frontend():
    try:
        return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
        logger.error(f"Error serving frontend: {str(e)}")
        return jsonify({"error": "Failed to serve frontend"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Prepare message for the LLM
        messages = [{"role": "user", "content": user_message}]
        
        # Get LLM response
        response = get_llm_response(messages, SYSTEM_PROMPT)
        
        # Store the conversation in Firestore
        try:
            chat_ref = db.collection('chats').add({
                'user_message': user_message,
                'bot_response': response,
                'timestamp': firestore.SERVER_TIMESTAMP  # Firestore's server timestamp
            })
            logger.info("Chat stored in Firestore successfully")
        except Exception as e:
            logger.error(f"Failed to store chat in Firestore: {str(e)}")
        
        return jsonify({"response": response})
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
