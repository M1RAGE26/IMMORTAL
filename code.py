from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Sample questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": [
            {"text": "Paris", "isCorrect": True},
            {"text": "London", "isCorrect": False},
            {"text": "Berlin", "isCorrect": False},
            {"text": "Madrid", "isCorrect": False}
        ]
    },
    {
        "question": "What is 2 + 2?",
        "options": [
            {"text": "3", "isCorrect": False},
            {"text": "4", "isCorrect": True},
            {"text": "5", "isCorrect": False},
            {"text": "6", "isCorrect": False}
        ]
    }
]

@app.route("/api/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)

@app.route("/api/submit-score", methods=["POST"])
def submit_score():
    data = request.get_json()
    username = data.get("username")
    score = data.get("score")
    print(f"{username} scored {score}")
    return jsonify({"message": "Score submitted successfully"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
