import json
from query_search import search_skills
import nltk
# from nltk import downloader

nltk.download("stopwords")
nltk.download('punkt')
def main():
    while True:
        query = input("Enter search query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        
        page = input("Enter page number: ")
        try:
            page = int(page)
            if page < 1:
                print("Page number must be 1 or greater.")
                continue
        except ValueError:
            print("Invalid page number. Please enter a valid integer.")
            continue
        
        results = search_skills(query.lower(), page)
        
        print(json.dumps(results, indent=4))

if __name__ == "__main__":
    main()
