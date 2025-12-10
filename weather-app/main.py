import os, requests
from flask import Flask, render_template

WEATHER_API_URL = os.getenv("WEATHER_API_URL", "http://localhost:8000/weather")

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
