from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Smart Event System Running"})

@app.route('/crowd')
def crowd():
    return jsonify({
        "Gate A": "Busy",
        "Gate B": "Free",
        "Gate C": "Moderate"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)