from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>this is the main flask file in the main folder with this added text plus MORE TESTTTTT"
