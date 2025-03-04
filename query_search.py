from sentence_transformers import SentenceTransformer
import typesense
import os
import json
import pprint

from nltk.tokenize import word_tokenize

from consts import (STOP_WORDS_SET,PUNCTUATION_SYMBOLS,THRESHOLD)

# Load sentence-transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")  # Change this based on your embedding model

# Setup Typesense client
client = typesense.Client({
    "nodes": [{
        "host": os.getenv("TYPESENSE_HOST", "localhost"),
        "port": os.getenv("TYPESENSE_PORT", "8108"),
        "protocol": "http"
    }],
    "api_key": os.getenv("TYPESENSE_API_KEY"),
    "connection_timeout_seconds": 2
})


def tokenize_query(query: str):
    return word_tokenize(query)

# print(client.collections["skills"].documents.search({"q": "*", "query_by": "bio"}))
def search_skills(query, page_number=1):
    # Convert query to embedding
    query_vector = model.encode(query).tolist()  # Convert to list for JSON serialization

    search_params = {
        "searches": [{
            "collection": "skills",
            "q": "*",  # Use wildcard because we are using vector search
            "vector_query": f"embedding:([{','.join(map(str, query_vector))}])",
            # "sort_by": "vector_distance:asc",
            "per_page": 10,
            "page":page_number
        }]
    }

    # Perform multi-search with required common_params argument
    results = client.multi_search.perform(search_params, {})  # Empty common_params
    # pprint.pprint(results)
    final_results = []
    for search_result in results["results"]:
        for hit in search_result["hits"]:
            similarity_score=1 - hit["vector_distance"]
            if similarity_score>THRESHOLD:
                final_results.append({
                    "user_id": hit["document"]["user_id"],
                    "user_bio": hit["document"]["bio"],
                    "similarity_score": similarity_score,  # Convert distance to similarity score
                    "matching_keyword": [word for word in word_tokenize(query.lower()) if word and word in hit["document"]["bio"].lower() and word not in STOP_WORDS_SET and word not in PUNCTUATION_SYMBOLS]
                })

    return sorted(final_results, key=lambda x: x["similarity_score"], reverse=True)  # Sort by highest similarity

