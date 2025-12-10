from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()


user = os.getenv("POSTGRES_USER", "admin")
password = os.getenv("POSTGRES_PASSWORD", "admin")
database = os.getenv("POSTGRES_DB", "weather_db")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")

database_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(url=database_url, pool_pre_ping=True)  # echo=True

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
