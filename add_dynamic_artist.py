import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_artist_meta(name):
    url = f"https://musicbrainz.org/ws/2/artist/?query=artist:{name}&fmt=json"
    headers = {'User-Agent': 'ArtistsPulse/1.0 (your-email@example.com)'}

    # Setup retries for network stability
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1,
                    status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        r = session.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json().get('artists', [])
        return data[0] if data else None
    except Exception as e:
        print(f"⚠️ API Connection Issue: {e}")
        return None


def save_to_db(name, genre):
    meta = get_artist_meta(name)

    if not meta:
        print(
            f"❌ Could not fetch data for {name}. Data not saved to keep DB clean.")
        return

    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        cur = conn.cursor()

        country = meta.get('country', '??')
        mb_id = meta.get('id', 'None')

        cur.execute(
            "INSERT INTO artists (name, genre, country, mb_id) VALUES (%s, %s, %s, %s)",
            (name, genre, country, mb_id)
        )

        conn.commit()
        print(f"✅ Success! Saved {name} | Country: {country} | MB_ID: {mb_id}")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ DB Error: {e}")


if __name__ == "__main__":
    artist_name = input("Enter artist name: ")
    artist_genre = input("Enter genre: ")
    save_to_db(artist_name, artist_genre)
