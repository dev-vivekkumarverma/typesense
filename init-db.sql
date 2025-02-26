DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'test_db') THEN
      CREATE DATABASE test_db;
   END IF;
END
$$;

\c test_db;

DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'test_user') THEN
      CREATE USER test_user WITH ENCRYPTED PASSWORD 'test@123';
   END IF;
END
$$;

GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;

CREATE TABLE IF NOT EXISTS skills (
    user_id SERIAL PRIMARY KEY,
    bio TEXT NOT NULL
);

INSERT INTO skills (bio)
SELECT unnest(array[
    'Experienced data engineer skilled in Databricks, SQL, and Apache Spark.',
    'Machine learning specialist with Python, TensorFlow, and SQL experience.',
    'Software engineer with expertise in Java, Spring Boot, and Kubernetes.',
    'Cloud architect experienced in AWS, Terraform, and CI/CD pipelines.',
    'Full-stack developer with React, Node.js, and PostgreSQL knowledge.',
    'Data scientist with strong skills in SQL, Databricks, and Python.',
    'Database administrator with experience in SQL, PostgreSQL, and MySQL.',
    'DevOps engineer proficient in Docker, Kubernetes, and Terraform.',
    'AI researcher skilled in NLP, OpenAI models, and deep learning.',
    'Cybersecurity expert with knowledge of SIEM, SOC, and threat hunting.',
    'Experienced software engineer skilled in Python, SQL, and cloud computing',
    'Data analyst with expertise in SQL, Python, and data visualization',
    'Backend developer specializing in Python frameworks and database optimization'
])
WHERE NOT EXISTS (SELECT 1 FROM skills);
