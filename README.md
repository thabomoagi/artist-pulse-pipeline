# artist-pulse-pipeline
Automated AWS data pipeline to track artist engagement across social platforms using Python and PostgreSQL.

## Key Features
* **Dynamic Ingestion:** Fetches real-time artist metadata (Country, MBID) via MusicBrainz API.
* **PostgreSQL Integration:** CRUD operations using `psycopg2` with parameterized queries for security.
* **SQL Analytics:** Built-in scripts for data aggregation and country-based reporting.
* **Safety First:** Implements `rollback` and `.env` protection for database credentials.
