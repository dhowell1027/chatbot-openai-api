from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the root route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Server is running!"})

# Define the /chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Adjust the function call for the new API
        response = openai.Completion.create(
            engine="gpt-4o-realtime-preview",  # Update the model/engine name if needed
            prompt=user_message,
            max_tokens=150
        )
        reply = response["choices"][0]["text"].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
