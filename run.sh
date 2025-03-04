docker-compose up -d
pip install -r requirements.txt
export NLTK_DATA="$HOME/nltk_data"
python -m nltk.downloader stopwords punkt_tab
python data_ingestion.py
python main.py
docker-compose down -v