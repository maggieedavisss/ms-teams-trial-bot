from flask import Flask, request, jsonify
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)  

@app.route("/", methods=["GET"])
def home():
    return "Bot is running on Azure!"

@app.route("/api/messages", methods=["POST"])
def messages():
    data = request.json
    if not data or "text" not in data:
        return jsonify({"response": "Invalid request"}), 400

    user_message = data["text"]
    bot_response = handle_message(user_message)

    return jsonify({"response": bot_response})

def handle_message(message):
    if "hello" in message.lower():
        return "Hello! How can I help you today?"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm a simple bot hosted on Azure!"

if __name__ == "__main__":
    port = Config.PORT  
    print(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port)
