from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/end1")
def home():
    return "Selamat datang kristo pemain boket!!"

@app.route("/end2")
def get_data():
    data = [
        {"nama": "Daniel", "usia": 25},
        {"nama": "Caesar", "usia": 30},
        {"nama": "Sila", "usia": 21},
    ]
    return jsonify({"data": data})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
