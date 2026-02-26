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

# The Refined Global List
global_stars = [
    ("Olivia Dean", "Soul/R&B"),
    ("Tyla", "Popiano"),
    ("Black Coffee", "House"),
    ("J. Cole", "Hip-Hop"),
    ("Drake", "Hip-Hop/Rap"),
    ("Kabza De Small", "Amapiano"),  # Swapped
    ("Adele", "Soul/Pop"),           # Swapped
    ("Doja Cat", "Pop/Rap"),
    ("DJ Maphorisa", "Amapiano"),    # Swapped
    ("SZA", "R&B")
]

cur.executemany(
    "INSERT INTO artists (name, genre) VALUES (%s, %s)", global_stars)
conn.commit()

print(f"🌍 Added {len(global_stars)} updated global stars!")

cur.close()
conn.close()
