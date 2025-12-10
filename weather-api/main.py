from utils.load_env import load_env

load_env("../.env")

from models import weather
from utils.get_db import engine
from routes.weather import router as weather_router
import uvicorn
from fastapi import FastAPI

app = FastAPI()


weather.Base.metadata.create_all(bind=engine)
app.include_router(weather_router)


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
