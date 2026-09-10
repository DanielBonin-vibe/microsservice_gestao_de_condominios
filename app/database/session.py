import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return psycopg.connect(
    dbname=os.gettenv('DB_NAME'),
    password=os.getenv('DB_PASSWORD'),
    user=os.getenv('DB_USER'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
    )