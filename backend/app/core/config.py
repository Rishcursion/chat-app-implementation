import os

from dotenv import load_dotenv

load_dotenv("./.env")


class Variables:
    PROJECT_NAME = "Chat-App"
    PROJECT_VER = "0.0.1"
    DB_DIALECT = "Postgres"
    SERVER_PORT = "8000"
    SERVER_DOMAIN = f"http://localhost:{SERVER_PORT}/"
    # ENV Variables
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")
    DB_SERVER = os.getenv("DB_SERVER")
    DB_URL = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
    )
    # Secrets
    JWT_SECRET = os.getenv("JWT_SECRET")


variables = Variables()
