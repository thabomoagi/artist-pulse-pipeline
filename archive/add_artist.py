import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    cur = conn.cursor()

    # 1. Insert data
    cur.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)",
                ("Clement Maosa", "Amapiano"))

    # 2. FORCE SAVE
    conn.commit()

    # 3. Double check it's there before leaving
    cur.execute("SELECT count(*) FROM artists;")
    count = cur.fetchone()[0]
    print(f"✅ Success! Total artists in DB: {count}")

    cur.close()
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")
