import typesense
from config import TYPESENSE

def get_typesense_client():
    return typesense.Client({
        "nodes": [{
            "host": TYPESENSE["host"],
            "port": TYPESENSE["port"],
            "protocol": "http"
        }],
        "api_key": TYPESENSE["api_key"],
        "connection_timeout_seconds": 5
    })
