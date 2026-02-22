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

# Ask for everything in the table
cur.execute("SELECT * FROM artists;")
rows = cur.fetchall()

print("--- ☁️ Data from AWS ☁️ ---")
for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Genre: {row[2]}")

cur.close()
conn.close()
