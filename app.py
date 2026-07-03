import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# UPGRADE: Added System Instruction to force concise, clean human-like answers
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are a helpful, concise classroom assistant. Keep all responses under 3 sentences unless asked otherwise. Do not use markdown text formatting like asterisks."
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    
    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        # UPGRADE: Cleaned up error messages so quota limits don't crash the user interface awkwardly
        if "429" in str(e):
            return jsonify({"reply": "⚠️ Rate limit reached. Please wait 30 seconds before sending another message."})
        return jsonify({"reply": "The AI is currently busy. Please try again in a moment."})

if __name__ == "__main__":
    app.run(debug=True)

