from pydantic import BaseModel, Field


class WeatherResponse(BaseModel):
    temperature: float = Field(..., description="Current temperature in Celsius")
    humidity: float = Field(..., description="Current humidity percentage")
    wind_speed: float = Field(..., description="Current wind speed in km/h")
    timestamp: int = Field(..., description="Unix timestamp of the weather data")
