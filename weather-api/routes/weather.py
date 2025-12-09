from fastapi import APIRouter
from fastapi.responses import JSONResponse
import random
import math
import time


router = APIRouter()

P = {
    "temp": {"mu": 15.0, "theta": 0.05, "sigma": 0.8},
    "humidity": {"mu": 60.0, "theta": 0.03, "sigma": 3.0},
    "wind": {"mu": 4.0, "theta": 0.04, "sigma": 0.5},
}

state = {"temp": 15.0, "humidity": 60.0, "wind": 4.0, "last": time.time()}


def ou_step(x, mu, theta, sigma, dt):
    drift = theta * (mu - x) * dt
    shock = sigma * math.sqrt(dt) * random.gauss(0, 1)
    return x + drift + shock


def fake_weather():
    now = time.time()
    dt = now - state["last"]
    state["last"] = now

    for key, p in P.items():
        state[key] = ou_step(state[key], p["mu"], p["theta"], p["sigma"], dt)

    return {
        "temp": round(state["temp"], 1),
        "humidity": int(state["humidity"]),
        "wind": round(state["wind"], 1),
    }


@router.get("/weather")
def get_weather():
    return JSONResponse(fake_weather())
