# from db import get_pg_connection
# from typesense_client import get_typesense_client
# import typesense

# COLLECTION_NAME = "skills_collection"

# def create_typesense_collection(client):
#     try:
#         client.collections[COLLECTION_NAME].delete()
#     except typesense.exceptions.ObjectNotFound:
#         pass

#     client.collections.create({
#         "name": COLLECTION_NAME,
#         "fields": [
#             {"name": "user_id", "type": "int32"},
#             {"name": "bio", "type": "string"}
#         ],
#         "default_sorting_field": "user_id"
#     })

# def populate_typesense():
#     pg_conn = get_pg_connection()
#     cursor = pg_conn.cursor()
#     cursor.execute("SELECT user_id, LOWER(bio) FROM skills;")
#     records = cursor.fetchall()

#     client = get_typesense_client()
#     create_typesense_collection(client)

#     documents = [{"user_id": r[0], "bio": r[1]} for r in records]
#     client.collections[COLLECTION_NAME].documents.import_(documents, {'action': 'upsert'})

#     pg_conn.close()

# if __name__ == "__main__":
#     populate_typesense()


from db import get_pg_connection
from typesense_client import get_typesense_client
from sentence_transformers import SentenceTransformer
import numpy as np

COLLECTION_NAME = "skills_collection"
model = SentenceTransformer("all-MiniLM-L6-v2")  # Fast & effective model

def create_typesense_collection(client):
    """Creates a new Typesense collection for storing embeddings."""
    try:
        client.collections[COLLECTION_NAME].delete()
    except:
        pass

    client.collections.create({
        "name": COLLECTION_NAME,
        "fields": [
            {"name": "user_id", "type": "int32"},
            {"name": "bio", "type": "string"},
            {"name": "embedding", "type": "float[]"}  # Store vector embeddings
        ],
        "default_sorting_field": "user_id"
    })

def populate_typesense():
    """Fetches data from PostgreSQL, generates embeddings, and stores them in Typesense."""
    pg_conn = get_pg_connection()
    cursor = pg_conn.cursor()
    cursor.execute("SELECT user_id, bio FROM skills;")
    records = cursor.fetchall()

    client = get_typesense_client()
    create_typesense_collection(client)

    documents = []
    for user_id, bio in records:
        embedding = model.encode(bio).tolist()  # Convert to list for storage
        documents.append({"user_id": user_id, "bio": bio, "embedding": embedding})

    client.collections[COLLECTION_NAME].documents.import_(documents, {'action': 'upsert'})
    pg_conn.close()

if __name__ == "__main__":
    populate_typesense()
