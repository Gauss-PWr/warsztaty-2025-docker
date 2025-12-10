from requests import Session
from fastapi import APIRouter, Depends
from utils.fake_weather import fake_weather
from utils.get_db import get_db
from schemas.weather import WeatherResponse
from models.weather import Weather

router = APIRouter()


@router.get("/weather")
def get_weather(db: Session = Depends(get_db)):

    data = fake_weather()

    weather_response = WeatherResponse(**data)

    weather = Weather(**data)

    db.add(weather)
    db.commit()
    db.refresh(weather)

    return weather_response
