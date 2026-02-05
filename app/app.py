from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Lab"

@app.route("/login")
def login():
    user = request.args.get("user")
    query = "SELECT * FROM users WHERE username = '%s'" % user
    return query

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
   AWS_ACCESS_KEY_ID = "AKIA1234567890TEST"

