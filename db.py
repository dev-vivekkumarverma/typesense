import psycopg2
from config import POSTGRES

def get_pg_connection():
    return psycopg2.connect(**POSTGRES)
