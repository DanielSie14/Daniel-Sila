from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/1")
def home():
    return "Selamat datang Ingrid!"

@app.route("/2")
def get_data():
    data = [
        {"nama": "Daniel", "usia": 25},
        {"nama": "Caesar", "usia": 30},
        {"nama": "Sila", "usia": 21},
    ]
    return jsonify({"data": data})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
