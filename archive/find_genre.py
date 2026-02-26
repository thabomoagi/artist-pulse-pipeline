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

# The WHERE clause: our first filter
cur.execute("SELECT name FROM artists WHERE genre = 'Amapiano';")
results = cur.fetchall()

print("🎹 Amapiano Kings in the Cloud:")
for row in results:
    print(f"- {row[0]}")

cur.close()
conn.close()
