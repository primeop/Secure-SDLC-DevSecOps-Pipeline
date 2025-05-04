import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/insecure", methods=["GET"])
def insecure_request():
    host = request.args.get("host")
    r = requests.get("http://" + host)
    return r.text

if __name__ == "__main__":
    app.run(debug=True)
