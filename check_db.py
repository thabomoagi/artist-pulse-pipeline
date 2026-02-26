import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def check_data():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    cur = conn.cursor()

    # The SQL "Read" command
    cur.execute("SELECT * FROM artists;")

    # fetchall() grabs every row the cursor found
    rows = cur.fetchall()

    print("\n--- 🔎 Current Database Rows ---")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    check_data()
