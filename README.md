# Employee Skill Search with PostgreSQL & Typesense

##  Project Overview
This project enables **semantic search for employee skills** using **PostgreSQL**, **Typesense**, and **Sentence Transformers**. The system efficiently finds employees based on their skills using **cosine similarity** on embeddings.

## ⚡ Features
- Store employee skills in **PostgreSQL**
- Index and search skills in **Typesense**
- Compute **semantic similarity** using **Sentence Transformers**
- **Dockerized PostgreSQL & Typesense**, with Python running locally

##  Project Structure
```
.
├── .env                      # Environment variables
├── docker-compose.yml        # Docker setup for PostgreSQL & Typesense
├── requirements.txt          # Python dependencies
├── db.py                     # PostgreSQL connection
├── typesense_client.py       # Typesense client setup
├── populate.py               # Fetches data from PostgreSQL & indexes it in Typesense
├── search.py                 # Searches for skills based on query
├── main.py                   # CLI interface to run the search
└── README.md                 # Project documentation
```

##  Setup & Installation

###  Install Dependencies
```sh
pip install -r requirements.txt
```

###  Start PostgreSQL & Typesense
```sh
docker-compose up -d
```

###  Populate Typesense with Employee Skills
```sh
python populate.py
```

###  Run the Skill Search
```sh
python main.py
```

##  Search Example
```
Enter skills to search (comma-separated)(exit to exit): sql,cybersecurity
Enter number of records per page: 2
```
### Example Output
```json
[RESULT #PAGE-1]

{"page_number": 1,
 "record_count_in_page": 2,
 "records": [{"bio": "Cybersecurity expert with knowledge of SIEM, SOC, and "
                     "threat hunting.",
              "similarity_score": 0.497,
              "user_id": 10},
             {"bio": "Data scientist with strong skills in SQL, Databricks, "
                     "and Python.",
              "similarity_score": 0.452,
              "user_id": 6}],
 "total_records": 10}
[RESULT #PAGE-2]

{"page_number": 2,
 "record_count_in_page": 2,
 "records": [{"bio": "Experienced software engineer skilled in Python, SQL, "
                     "and cloud computing",
              "similarity_score": 0.438,
              "user_id": 11},
             {"bio": "Data analyst with expertise in SQL, Python, and data "
                     "visualization",
              "similarity_score": 0.435,
              "user_id": 12}],
 "total_records": 10}
[RESULT #PAGE-3]

{"page_number": 3,
 "record_count_in_page": 2,
 "records": [{"bio": "Database administrator with experience in SQL, "
                     "PostgreSQL, and MySQL.",
              "similarity_score": 0.41,
              "user_id": 7},
             {"bio": "Backend developer specializing in Python frameworks and "
                     "database optimization",
              "similarity_score": 0.359,
              "user_id": 13}],
 "total_records": 10}
[RESULT #PAGE-4]

{"page_number": 4,
 "record_count_in_page": 2,
 "records": [{"bio": "Full-stack developer with React, Node.js, and PostgreSQL "
                     "knowledge.",
              "similarity_score": 0.279,
              "user_id": 5},
             {"bio": "DevOps engineer proficient in Docker, Kubernetes, and "
                     "Terraform.",
              "similarity_score": 0.181,
              "user_id": 8}],
 "total_records": 10}
[RESULT #PAGE-5]

{"page_number": 5,
 "record_count_in_page": 2,
 "records": [{"bio": "Cloud architect experienced in AWS, Terraform, and CI/CD "
                     "pipelines.",
              "similarity_score": 0.172,
              "user_id": 4},
             {"bio": "AI researcher skilled in NLP, OpenAI models, and deep "
                     "learning.",
              "similarity_score": 0.142,
              "user_id": 9}],
 "total_records": 10}
```

## ⚙️ Configuration
Set up `.env` files for **both the project and Docker**:

#### **Project `.env`**
```
POSTGRES_DB=test_db
POSTGRES_USER=test_user
POSTGRES_PASSWORD=test@123
POSTGRES_PORT=5432
TYPESENSE_HOST=localhost
TYPESENSE_PORT=8108
TYPESENSE_API_KEY=xyz123
```

#### **Docker `.env`**
```
POSTGRES_USER=test_user
POSTGRES_PASSWORD=test@123
POSTGRES_DB=test_db
```

##  Technologies Used
- **Python** 🐍
- **PostgreSQL** 🛢️
- **Typesense** 🔍
- **Sentence Transformers** 🤖
- **Docker-compose** 🐳

