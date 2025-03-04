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
    'Backend developer specializing in Python frameworks and database optimization',
    'Dr. Sarah Collins is a board-certified cardiologist with 10 years of experience specializing in heart failure and arrhythmia management. She has contributed to multiple research papers and actively participates in clinical trials. Passionate about preventive healthcare, she educates patients on lifestyle changes to reduce cardiovascular risks.',
    'Dr. Michael Patel is an orthopedic surgeon with expertise in joint replacement and sports medicine. He has performed over 500 successful surgeries and works closely with rehabilitation specialists to ensure patient recovery. His research focuses on minimally invasive techniques for faster healing and improved outcomes.',
    'Dr. Emily Carter is a pediatrician with 15 years of experience treating children with chronic illnesses. She has developed community programs to support child health and wellness. Her research in childhood obesity prevention has influenced national healthcare policies.',
    'Dr. John Peterson is a neurologist specializing in neurodegenerative diseases. With over a decade of experience, he works on developing new treatments for Alzheimer and Parkinson disease. His research focuses on early detection and intervention strategies.',
    'Dr. Sophia Kim is a dermatologist with expertise in cosmetic and medical dermatology. She has treated thousands of patients for conditions such as acne, eczema, and skin cancer. She is passionate about developing personalized skincare routines for patients.',
    
   --  # Civil Engineering Bios
    'Emily Carter is a structural engineer with a decade of experience in designing earthquake-resistant buildings. She has worked on major infrastructure projects, including bridges and high-rise buildings. Passionate about sustainable construction, she integrates eco-friendly materials and energy-efficient designs into her projects.',
    'John Peterson is a civil engineer specializing in transportation systems and urban planning. With over 12 years of experience, he has designed highways, metro stations, and smart city frameworks. His work emphasizes efficiency, sustainability, and safety for commuters.',
    'Michael Lee is a geotechnical engineer with expertise in soil mechanics and foundation design. He has consulted on major dam and tunnel projects worldwide. His research focuses on landslide prevention and sustainable foundation solutions.',
    'Rachel Adams is a water resource engineer working on flood control and water conservation projects. She has designed systems for efficient water distribution in arid regions. Passionate about climate change resilience, she integrates sustainable water management techniques into infrastructure planning.',
    'David Harris is a construction manager overseeing large-scale commercial and residential developments. With 18 years of experience, he ensures projects are completed on time and within budget. He specializes in green building technologies and energy-efficient designs.',
    
   --  # Electrical Engineering Bios
    'Dr. Rajesh Kumar is an electrical engineer focusing on power systems and renewable energy. With a PhD in smart grid technology, he has developed innovative solutions for integrating solar and wind energy into traditional power grids. His research aims to improve energy efficiency and reduce carbon footprints.',
    'Sophia Nguyen is an embedded systems engineer with expertise in IoT and robotics. She has worked on developing smart home automation systems and industrial control solutions. Passionate about technology, she collaborates with startups to create cutting-edge embedded solutions for everyday applications.',
    'Robert Chen is an electrical engineer specializing in semiconductor design and fabrication. He has worked on developing next-generation microchips for mobile and computing applications. His research focuses on increasing chip efficiency and reducing power consumption.',
    'Amanda Lopez is a power electronics engineer with expertise in electric vehicle battery systems. She has contributed to developing fast-charging technologies for EVs. Passionate about sustainability, she works on improving renewable energy storage solutions.',
    'James Carter is a communications engineer focusing on 5G and satellite communication technologies. With a decade of experience, he has designed and implemented advanced wireless networks. His work contributes to improving global connectivity and internet access in remote areas.',
    
   --  # Computer Science Bios
    'David Miller is a software engineer with expertise in artificial intelligence and cloud computing. He has developed scalable machine learning models for fraud detection and recommendation systems. Passionate about open-source contributions, he actively contributes to AI and cloud security projects.',
    'Lisa Wong is a cybersecurity specialist with experience in ethical hacking and network security. She has helped organizations strengthen their cyber defenses by identifying vulnerabilities and implementing robust security protocols. Her work focuses on proactive threat detection and risk mitigation strategies.',
    'Kevin Brown is a data scientist specializing in big data analytics and predictive modeling. He has worked on projects involving customer behavior analysis and financial forecasting. His research focuses on improving machine learning models for better decision-making.',
    'Jessica White is a blockchain developer with experience in smart contracts and decentralized finance applications. She has worked on building secure and transparent financial transaction systems. Passionate about fintech, she researches innovative applications of blockchain technology.',
    'Ethan Green is a game developer specializing in AI-driven gameplay mechanics. He has developed popular mobile and PC games with immersive experiences. Passionate about virtual reality, he explores new ways to enhance user interaction in gaming environments.'
])
WHERE NOT EXISTS (SELECT 1 FROM skills);
