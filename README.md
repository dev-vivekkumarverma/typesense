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
├── init-db.sql               # Postgresql Query that inserts the data in postgresh for initial move
├── data_ingestion.py         # Fetches data from PostgreSQL & indexes it in Typesense
├── query_search.py           # Searches for skills based on query
├── embedding_utils.py        # Used for finding the embeddings of the data to pe put in Typesense
├── consts.py                 # Constants that are used in the Project
├── main.py                   # CLI interface to run the search
├── run.sh                    # Contains all the commands that can be run after virtual environment activation to run the project in one go and
|                                    #release all the resources after exit commnd
└── README.md                 # Project documentation
```

##  Setup & Installation

### create a virtual environment and activate it
```sh 
python -m venv venv

source ./venv/bin/activate

```
---
- there are two ways to run the project after activating the virtual environment
---
## 1st method (for running in one go for testing)
```sh
chmod +x run.sh
./run.sh
```
---
## 2nd method (for running it step by step)

###  Install Dependencies
```sh
pip install -r requirements.txt
```

###  Start PostgreSQL & Typesense
```sh
docker-compose up -d
```

### Set the path for NLTK_DATA and install some required files
```sh
export NLTK_DATA="$HOME/nltk_data"
python -m nltk.downloader stopwords punkt_tab
```
###  Populate Typesense with Employee Skills
```sh
python data_ingestion.py
```

###  Run the Skill Search
```sh
python main.py
```

##  Search Example
```
Enter search query (or 'exit' to quit): give me people with sql, python and django framework skills
Enter page number: 1
```
### Example Output
```json
[
    {
        "user_id": 11,
        "user_bio": "Experienced software engineer skilled in Python, SQL, and cloud computing",
        "similarity_score": 0.669215738773346,
        "matching_keyword": [
            "sql",
            "python"
        ]
    },
    {
        "user_id": 13,
        "user_bio": "Backend developer specializing in Python frameworks and database optimization",
        "similarity_score": 0.6598625779151917,
        "matching_keyword": [
            "python",
            "framework"
        ]
    },
    {
        "user_id": 2,
        "user_bio": "Machine learning specialist with Python, TensorFlow, and SQL experience.",
        "similarity_score": 0.6584064960479736,
        "matching_keyword": [
            "sql",
            "python"
        ]
    },
    {
        "user_id": 6,
        "user_bio": "Data scientist with strong skills in SQL, Databricks, and Python.",
        "similarity_score": 0.601262092590332,
        "matching_keyword": [
            "sql",
            "python",
            "skills"
        ]
    },
    {
        "user_id": 12,
        "user_bio": "Data analyst with expertise in SQL, Python, and data visualization",
        "similarity_score": 0.5005065202713013,
        "matching_keyword": [
            "sql",
            "python"
        ]
    },
    {
        "user_id": 1,
        "user_bio": "Experienced data engineer skilled in Databricks, SQL, and Apache Spark.",
        "similarity_score": 0.4846632480621338,
        "matching_keyword": [
            "sql"
        ]
    },
    {
        "user_id": 7,
        "user_bio": "Database administrator with experience in SQL, PostgreSQL, and MySQL.",
        "similarity_score": 0.4649410843849182,
        "matching_keyword": [
            "sql"
        ]
    },
    {
        "user_id": 5,
        "user_bio": "Full-stack developer with React, Node.js, and PostgreSQL knowledge.",
        "similarity_score": 0.41084957122802734,
        "matching_keyword": [
            "sql"
        ]
    }
]
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
- **NLTK**

