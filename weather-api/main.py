from routes.weather import router as weather_router
import uvicorn
from fastapi import FastAPI

app = FastAPI()

app.include_router(weather_router)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
