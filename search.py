# from typesense_client import get_typesense_client
# from db import get_pg_connection

# COLLECTION_NAME = "skills_collection"

# def search_skills(query, records_per_page):
#     query_skills = set(map(str.lower, query.split(", ")))

#     search_params = {
#         "q": " ".join(query_skills),
#         "query_by": "bio",
#         "per_page": 100
#     }

#     client = get_typesense_client()
#     results = client.collections[COLLECTION_NAME].documents.search(search_params)

#     matched_records = []
#     for hit in results["hits"]:
#         bio = hit["document"]["bio"]
#         user_id = hit["document"]["user_id"]
#         bio_skills = set(bio.split())
#         matching_skills = query_skills.intersection(bio_skills)
#         similarity_score = len(matching_skills) / len(query_skills)

#         matched_records.append((similarity_score, user_id, bio, list(matching_skills)))

#     matched_records.sort(reverse=True, key=lambda x: x[0])

#     total_records = len(matched_records)
#     paginated_records = matched_records[:records_per_page]

#     return {
#         "total_records": total_records,
#         "page_number": 1,
#         "record_count_in_page": len(paginated_records),
#         "records": [
#             {
#                 "user_id": r[1],
#                 "bio": r[2],
#                 "similarity_score": round(r[0], 3),
#                 "matching_skills": r[3]
#             }
#             for r in paginated_records
#         ]
#     }




from typesense_client import get_typesense_client
from sentence_transformers import SentenceTransformer
import numpy as np

COLLECTION_NAME = "skills_collection"
model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(vec1, vec2):
    """Computes cosine similarity between two vectors."""
    vec1, vec2 = np.array(vec1), np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def search_skills(query, records_per_page):
    """Searches for skills based on query and ranks by cosine similarity."""
    query_embedding = model.encode(str(query).lower()).tolist()
    query_skills = set()
    for section in query.lower().split(","):
        query_skills.update(section.split())
    search_params = {
        "q": "*",  # Fetch all documents
        "query_by": "bio",  # Necessary to retrieve documents
        # "per_page": records_per_page
    }

    client = get_typesense_client()
    results = client.collections[COLLECTION_NAME].documents.search(search_params)

    matched_records = []
    for hit in results["hits"]:
        bio = hit["document"]["bio"]
        user_id = hit["document"]["user_id"]
        embedding = hit["document"]["embedding"]

        similarity_score = float(cosine_similarity(query_embedding, embedding))
        bio_words = set()
        for section in bio.lower().split(','):
            bio_words.update(section.split())
        
        matching_skills = list(bio_words.intersection(query_skills))
        
        matched_records.append((similarity_score, user_id, bio, matching_skills))
        # print("bio_words", bio_words)
        # print("query_skills", query_skills)
        # print("matching skills", bio_words.intersection(query_skills))
    matched_records.sort(reverse=True, key=lambda x: x[0])  # Sort by similarity score

    total_records = len(matched_records)
    paginated_records =[]
    start=0
    page=1
    while start<total_records:
        end= min(start+records_per_page,total_records)
        page_record=matched_records[start:end]
        paginated_records.append({
            "total_records": total_records,
            "page_number": page,
            "record_count_in_page": len(page_record),
            "records": [
                {
                    "user_id": r[1],
                    "bio": r[2],
                    "similarity_score": round(r[0], 3),
                    "matching_keywords": r[3]
                }
                for r in page_record
            ]
        })
        page+=1
        start=end

    return paginated_records
