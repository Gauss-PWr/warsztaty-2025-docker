from sqlalchemy import Integer
from utils.get_db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Weather(Base):
    __tablename__ = "weather"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    temperature: Mapped[float] = mapped_column()
    humidity: Mapped[int] = mapped_column(Integer)
    wind_speed: Mapped[float] = mapped_column()
    timestamp: Mapped[int] = mapped_column(Integer)
