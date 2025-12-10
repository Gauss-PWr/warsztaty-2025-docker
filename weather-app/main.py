import os, requests
from flask import Flask, render_template

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "8000")
WEATHER_API_URL = f"http://{API_HOST}:{API_PORT}/weather"

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/data")
def data():
    r = requests.get(WEATHER_API_URL, timeout=5)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
