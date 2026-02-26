import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def delete_by_id(artist_id):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    cur = conn.cursor()

    # %s is our "Shield" against SQL Injection
    sql = "DELETE FROM artists WHERE artist_id = %s;"

    try:
        cur.execute(sql, (artist_id,))
        conn.commit()
        print(f"🗑️ Successfully deleted artist with ID: {artist_id}")
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()  # The safety net!
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    target = input("Enter the ID you want to delete: ")
    delete_by_id(target)
