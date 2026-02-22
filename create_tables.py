import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS artists (
            artist_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            genre VARCHAR(100),
            followers_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
    )

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        cur = conn.cursor()

        # Execute the command
        for command in commands:
            cur.execute(command)

        # Commit (save) the changes
        conn.commit()

        print("✅ Table 'artists' created successfully!")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    create_tables()
