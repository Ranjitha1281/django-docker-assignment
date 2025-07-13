import time
import psycopg2
from psycopg2 import OperationalError

while True:
    try:
        conn = psycopg2.connect(
            dbname="mydb",
            user="myuser",
            password="mypassword",
            host="db",
            port="5432"
        )
        print("✅ PostgreSQL is ready.")
        conn.close()
        break
    except OperationalError:
        print("⏳ DB not ready, retrying...")
        time.sleep(1)
