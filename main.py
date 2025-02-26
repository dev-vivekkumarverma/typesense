from populate import populate_typesense
from search import search_skills
import time
from pprint import pprint

if __name__ == "__main__":
    print("Populating Typesense with PostgreSQL data...")
    populate_typesense()
    time.sleep(5) # sleeping for 5 sec to let all the services be up and running
    while True:
        query = input("Enter skills to search (comma-separated)(exit to exit): ")
        if query.strip().lower()=="exit":
            break
        records_per_page = int(input("Enter number of records per page: "))

        results = search_skills(query, records_per_page)
        for idx, page_data in enumerate(results):
            print(f"[RESULT #PAGE-{idx+1}]\n")
            pprint(page_data)
