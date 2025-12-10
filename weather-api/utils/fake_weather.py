import random
import math
import time


P = {
    "temperature": {"mu": 15.0, "theta": 0.05, "sigma": 0.8},
    "humidity": {"mu": 60.0, "theta": 0.03, "sigma": 3.0},
    "wind_speed": {"mu": 4.0, "theta": 0.04, "sigma": 0.5},
}

state = {"temperature": 15.0, "humidity": 60.0, "wind_speed": 4.0, "last": time.time()}


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
        "temperature": round(state["temperature"], 1),
        "humidity": int(state["humidity"]),
        "wind_speed": round(state["wind_speed"], 1),
        "timestamp": int(now),
    }
