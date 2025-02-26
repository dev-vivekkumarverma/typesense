# Employee Skill Search with PostgreSQL & Typesense

## 📌 Project Overview
This project enables **semantic search for employee skills** using **PostgreSQL**, **Typesense**, and **Sentence Transformers**. The system efficiently finds employees based on their skills using **cosine similarity** on embeddings.

## ⚡ Features
- Store employee skills in **PostgreSQL**
- Index and search skills in **Typesense**
- Compute **semantic similarity** using **Sentence Transformers**
- **Dockerized PostgreSQL & Typesense**, with Python running locally

## 🏗️ Project Structure
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

## 🛠️ Setup & Installation

### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Start PostgreSQL & Typesense
```sh
docker-compose up -d
```

### 3️⃣ Populate Typesense with Employee Skills
```sh
python populate.py
```

### 4️⃣ Run the Skill Search
```sh
python main.py
```

## 🔍 Search Example
```
Enter skills to search (comma-separated): Python, SQL
Enter number of records per page: 3
```
### ✅ Example Output
```json
{
    "total_records": 10,
    "page_number": 1,
    "record_count_in_page": 3,
    "records": [
        {
            "user_id": 101,
            "bio": "Experienced software engineer skilled in Python, SQL, and cloud computing",
            "similarity_score": 0.92
        },
        {
            "user_id": 205,
            "bio": "Data analyst with expertise in SQL, Python, and data visualization",
            "similarity_score": 0.88
        },
        {
            "user_id": 342,
            "bio": "Backend developer specializing in Python frameworks and database optimization",
            "similarity_score": 0.85
        }
    ]
}
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

## 📌 Technologies Used
- **Python** 🐍
- **PostgreSQL** 🛢️
- **Typesense** 🔍
- **Sentence Transformers** 🤖
- **Docker** 🐳

