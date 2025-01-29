from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def index():
    response = {
        "email": "preciousezeigbo81@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/PreciousEzeigbo/HNG12_Stage0"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
