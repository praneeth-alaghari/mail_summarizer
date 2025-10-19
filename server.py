# app.py
from flask import Flask, jsonify
from email_summarizer.email_summary import get_summary

app = Flask(__name__)

@app.route("/run-mail-summarizer", methods=["GET"])
def run_summary():
    try:
        summary_text = get_summary()
        return jsonify({"summary": summary_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Mail Summarizer API! Use /run-mail-summarizer to get a summary."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
