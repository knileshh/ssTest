# Custom LLM-powered Chatbot

This project implements a custom LLM-powered chatbot with real-time data storage using Firebase.

## Project Structure

- `backend/`: Contains the Flask backend application
  - `app.py`: Main Flask application
  - `llm_integration.py`: LLM integration with Groq API
- `frontend/`: Contains the HTML frontend
  - `index.html`: Chatbot interface
- `firebase-credentials.json`: Firebase service account key (not included in repository)

## Setup Instructions

1. Clone the repository
2. Set up a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Set up Groq API:
   - Create an account at [Groq Cloud](https://console.groq.com/)
   - Obtain API key and set it as an environment variable:
     ```
     export GROQ_API_KEY=your_api_key_here
     ```
4. Set up Firebase:
   - Create a new Firebase project
   - Generate a new private key for your service account
   - Save the key as `firebase-credentials.json` in the project root
   - Update the path in `app.py` to point to your credentials file

## Running the Project Locally

1. Start the Flask backend:
   ```
   python backend/app.py
   ```
2. Open `frontend/index.html` in a web browser

## Deployment

- Backend: Deploy the Flask app to Heroku or Google Cloud Run
- Frontend: Deploy the HTML file to GitHub Pages or Netlify

## Demo Video

[Link to demo video showing the chatbot in action and real-time data storage]