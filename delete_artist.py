import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)
cur = conn.cursor()

# We target ID 1 specifically
cur.execute("DELETE FROM artists WHERE artist_id = 1;")
conn.commit()

print("🗑️ Deleted duplicate entry (ID: 1)")

cur.close()
conn.close()
