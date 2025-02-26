import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": "localhost",
    "port": os.getenv("POSTGRES_PORT"),
}

TYPESENSE = {
    "host": os.getenv("TYPESENSE_HOST"),
    "port": os.getenv("TYPESENSE_PORT"),
    "api_key": os.getenv("TYPESENSE_API_KEY"),
}
