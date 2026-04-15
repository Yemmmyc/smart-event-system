from flask import Flask, jsonify
from flask_cors import CORS
import random   # ✅ IMPORT AT THE TOP

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "Smart Event System Running"})

@app.route('/crowd')
def crowd():
    return jsonify({
        "Gate A": random.choice(["Busy", "Moderate"]),
        "Gate B": random.choice(["Free (Recommended)", "Moderate"]),
        "Gate C": random.choice(["Moderate", "Busy"])
    })

@app.route('/alerts')
def alerts():
    messages = [
        "Use Gate B for faster entry",
        "Crowd building up at Gate A",
        "Food court queue is high",
        "Exit via Gate C for faster movement"
    ]

    return jsonify({
        "message": random.choice(messages)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)