import psycopg2
import typesense
import os
from embedding_utils import generate_embedding
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    port=os.getenv("POSTGRES_PORT", "5432"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)
cursor = conn.cursor()

# Fetch user bios
cursor.execute("SELECT user_id, bio FROM skills;")
rows = cursor.fetchall()
print("Fetched rows:", rows)  # Debugging

if not rows:
    print("No data found in PostgreSQL. Check your database.")
    exit()

# Initialize Typesense client
client = typesense.Client({
    'nodes': [{'host': os.getenv("TYPESENSE_HOST"), 'port': os.getenv("TYPESENSE_PORT"), 'protocol': 'http'}],
    'api_key': os.getenv("TYPESENSE_API_KEY"),
    'connection_timeout_seconds': 2
})

# Define Typesense schema
schema = {
    "name": "skills",
    "fields": [
        {"name": "user_id", "type": "int32"},
        {"name": "bio", "type": "string"},  # Ensure consistent field names
        {"name": "embedding", "type": "float[]", "num_dim": 384}
    ]
}

# Create collection if not exists
try:
    client.collections.create(schema)
    print("Collection created successfully.")
except Exception as e:
    print("Collection already exists:", str(e))

# Insert data into Typesense
documents = []
for i, (user_id, bio) in enumerate(rows):
    print(f"Inserting document {i+1} for user_id: {user_id}")

    embedding = generate_embedding(bio)
    if not embedding or len(embedding) != 384:
        print(f"Error: Invalid embedding for user_id {user_id}. Skipping...")
        continue

    documents.append({"user_id": user_id, "bio": bio, "embedding": embedding})

# Import data in batches to prevent memory issues
batch_size = 50  # Adjust batch size if needed
for i in range(0, len(documents), batch_size):
    batch = documents[i : i + batch_size]
    try:
        client.collections['skills'].documents.import_(batch, {'action': 'upsert'})
        print(f"Inserted batch {i // batch_size + 1}")
    except Exception as e:
        print("Error inserting batch:", str(e))

print("Data ingestion complete.")
