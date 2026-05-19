# database.py
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DB_URL)

def save_complaint_and_find_clusters(text: str, location: str, embedding: list):
    """Şikayeti kaydeder ve aynı bölgedeki benzer şikayetleri bulur."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Yeni şikayeti kaydet
    cursor.execute(
        """INSERT INTO complaints (raw_text, location, embedding) 
           VALUES (%s, %s, %s) RETURNING id;""",
        (text, location, embedding)
    )
    new_id = cursor.fetchone()[0]
    
    # 2. Benzerlik araması (Kosinüs benzerliği < 0.15 demek, %85 üstü benzerlik demektir)
    # Not: Veritabanında vektör indexlemesi ve pgvector eklentisi kurulu olmalıdır.
    cursor.execute(
        """SELECT count(id) FROM complaints 
           WHERE location = %s AND id != %s AND embedding <=> %s::vector < 0.15;""",
        (location, new_id, embedding)
    )
    similar_count = cursor.fetchone()[0]
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"similar_complaints_count": similar_count}