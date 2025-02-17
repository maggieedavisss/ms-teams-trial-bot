from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/api/messages", methods=["POST"])
def messages():
    data = request.json
    if "text" in data:
        user_message = data["text"]
        bot_response = handle_message(user_message)
        return jsonify({"response": bot_response})
    return jsonify({"response": "I didn't understand that."})

def handle_message(message):
    if "hello" in message.lower():
        return "Hello! How can I help you today?"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm just a simple bot, but I'm learning!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
