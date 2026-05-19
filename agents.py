# agents.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from state import ComplaintState
from database import save_complaint_and_find_clusters
from dotenv import load_dotenv
import json

load_dotenv()

# Modelleri Başlat
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
# Google yerine HuggingFace'in en popüler hafif vektör modelini kullanıyoruz
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def understanding_agent(state: ComplaintState):
    prompt = f"""
    Şu şikayeti analiz et: "{state['raw_text']}"
    Bana sadece şu formatta JSON dön:
    {{"kategori": "Altyapı/Ulaşım/Çevre vs.", "aciliyet_skoru": 1-10 arasi bir sayi}}
    Aciliyet Kriteri: Ambulans, çökme, can güvenliği gibi konularda skor 9-10 olmalı. Sokak lambası gibi konularda 1-3 olmalı.
    """
    response = llm.invoke(prompt)
    
    # JSON verisini parse et (Hackathon ortamı için basit try-except)
    try:
        data = json.loads(response.content.replace("```json", "").replace("```", ""))
        state["complaint_type"] = data.get("kategori", "Bilinmeyen")
        state["urgency_score"] = data.get("aciliyet_skoru", 1)
    except:
        state["complaint_type"] = "Analiz Edilemedi"
        state["urgency_score"] = 5
        
    state["status"] = "Anlaşıldı"
    return state

def location_agent(state: ComplaintState):
    prompt = f"""
    Şu metinden sadece ilçe veya mahalle bilgisini çıkar: "{state['raw_text']}"
    Eğer konum yoksa 'Bilinmiyor' yaz. Sadece konumu söyle, başka kelime kullanma.
    """
    response = llm.invoke(prompt)
    state["location_details"] = response.content.strip()
    return state

def clustering_agent(state: ComplaintState):
    # Metni vektöre çevir
    vector = embeddings.embed_query(state["raw_text"])
    state["embedding_vector"] = vector
    
    # Veritabanına kaydet ve benzer şikayet sayısını (cluster) çek
    cluster_data = save_complaint_and_find_clusters(
        text=state["raw_text"], 
        location=state["location_details"], 
        embedding=vector
    )
    state["cluster_info"] = cluster_data
    return state

def routing_agent(state: ComplaintState):
    kategori = state["complaint_type"]
    if "Altyapı" in kategori or "Su" in kategori:
        state["assigned_unit"] = "ASKİ"
    elif "Ulaşım" in kategori:
        state["assigned_unit"] = "EGO"
    else:
        state["assigned_unit"] = "Fen İşleri"
        
    state["status"] = "Yönlendirildi"
    return state