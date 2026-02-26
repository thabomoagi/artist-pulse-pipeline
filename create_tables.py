import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_tables():
    commands = (
        "DROP TABLE IF EXISTS artists CASCADE;",
        """
        CREATE TABLE artists (
            artist_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            country VARCHAR(10),
            mb_id VARCHAR(50),
            followers_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        print("✅ Table 'artists' refreshed with Country and MusicBrainz ID columns!")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    create_tables()
