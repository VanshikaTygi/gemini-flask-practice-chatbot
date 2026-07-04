from flask import Flask, render_template, request, jsonify
from services.llm import GeminiService

app = Flask(__name__)
ai_service = GeminiService()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    mode = data.get("mode", "general") # Capture if user wants simple chat or code breakdown
    
    if not user_message:
        return jsonify({"error": "Empty message body"}), 400
        
    if mode == "explain":
        instruction = "You are an elite Senior Software Engineer. Break down the user's code snippet line-by-line. Keep it simple, architectural, and educational."
    else:
        instruction = "You are a concise classroom mentor. Give accurate answers under three lines. Avoid complex markdown notation."
        
    reply = ai_service.get_chat_response(user_message, system_instruction=instruction)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
