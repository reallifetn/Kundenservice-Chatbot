from flask import Flask, request, jsonify

app = Flask(__name__)

# Antworten aus Datei laden
with open("antworten.txt", "r", encoding="utf-8") as f:
    antworten = [zeile.strip() for zeile in f.readlines()]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    for a in antworten:
        if a.lower() in user_input:
            return jsonify({"reply": a})
    return jsonify({"reply": "Ich verstehe nicht. Kannst du das anders formulieren?"})

@app.route("/")
def home():
    return "Der Chatbot läuft! Sende POST-Anfragen an /chat"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

