# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
from graph import mavi_masa_app

app = FastAPI(title="Mavi Masa AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Next.js'in rahatça bağlanabilmesi için
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Frontend'den gelecek istek gövdesi (Payload)
class ComplaintRequest(BaseModel):
    text: str

@app.post("/api/v1/process-complaint")
async def process_complaint(request: ComplaintRequest):
    # LangGraph state'ini başlat
    initial_state = {
        "raw_text": request.text,
        "complaint_type": None,
        "urgency_score": None,
        "location_details": None,
        "embedding_vector": None,
        "cluster_info": None,
        "assigned_unit": None,
        "status": "Başladı"
    }
    
    # Grafı çalıştır
    result = mavi_masa_app.invoke(initial_state)
    
    # Frontend'e döndürülecek yanıt
    return {
        "kategori": result["complaint_type"],
        "aciliyet": result["urgency_score"],
        "konum": result["location_details"],
        "benzer_sikayet_sayisi": result["cluster_info"].get("similar_complaints_count", 0),
        "yonlendirilen_birim": result["assigned_unit"]
    }

# Çalıştırmak için komut (terminalde):
# uvicorn main:app --reload