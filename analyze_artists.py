import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def run_analysis():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    cur = conn.cursor()

    # SQL logic: Group by country and count them
    query = """
        SELECT country, COUNT(*) 
        FROM artists 
        GROUP BY country;
    """

    cur.execute(query)
    rows = cur.fetchall()

    print("\n--- 📊 Artist Count by Country ---")
    for row in rows:
        print(f"Country: {row[0]} | Count: {row[1]}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    run_analysis()
