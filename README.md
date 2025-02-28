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
Enter skills to search (comma-separated)(exit to exit): give me people with sql, python and databricks skills
Enter number of records per page: 10
```
### Example Output
```json
[RESULT #PAGE-1]

{"page_number": 1,
 "record_count_in_page": 10,
 "records": [{"bio": "Data scientist with strong skills in SQL, Databricks, "
                     "and Python.",
              "matching_keywords": ["with",
                                    "sql",
                                    "databricks",
                                    "and",
                                    "skills"],
              "similarity_score": 0.876,
              "user_id": 6},
             {"bio": "Experienced software engineer skilled in Python, SQL, "
                     "and cloud computing",
              "matching_keywords": ["python", "sql", "and"],
              "similarity_score": 0.658,
              "user_id": 11},
             {"bio": "Data analyst with expertise in SQL, Python, and data "
                     "visualization",
              "matching_keywords": ["python", "with", "sql", "and"],
              "similarity_score": 0.61,
              "user_id": 12},
             {"bio": "Backend developer specializing in Python frameworks and "
                     "database optimization",
              "matching_keywords": ["python", "and"],
              "similarity_score": 0.554,
              "user_id": 13},
             {"bio": "Database administrator with experience in SQL, "
                     "PostgreSQL, and MySQL.",
              "matching_keywords": ["with", "sql", "and"],
              "similarity_score": 0.475,
              "user_id": 7},
             {"bio": "Full-stack developer with React, Node.js, and PostgreSQL "
                     "knowledge.",
              "matching_keywords": ["with", "and"],
              "similarity_score": 0.444,
              "user_id": 5},
             {"bio": "DevOps engineer proficient in Docker, Kubernetes, and "
                     "Terraform.",
              "matching_keywords": ["and"],
              "similarity_score": 0.4,
              "user_id": 8},
             {"bio": "Cloud architect experienced in AWS, Terraform, and CI/CD "
                     "pipelines.",
              "matching_keywords": ["and"],
              "similarity_score": 0.321,
              "user_id": 4},
             {"bio": "AI researcher skilled in NLP, OpenAI models, and deep "
                     "learning.",
              "matching_keywords": ["and"],
              "similarity_score": 0.313,
              "user_id": 9},
             {"bio": "Cybersecurity expert with knowledge of SIEM, SOC, and "
                     "threat hunting.",
              "matching_keywords": ["with", "and"],
              "similarity_score": 0.262,
              "user_id": 10}],
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

