# state.py
from typing import TypedDict, Optional, List, Dict, Any

class ComplaintState(TypedDict):
    raw_text: str                  # Vatandaştan gelen ham şikayet
    complaint_type: Optional[str]  # Kategori (Örn: Altyapı, Ulaşım)
    urgency_score: Optional[int]   # 1-10 arası aciliyet
    location_details: Optional[str]# Çıkarılan konum bilgisi
    embedding_vector: Optional[List[float]] # pgvector için vektör
    cluster_info: Optional[Dict[str, Any]]  # Benzer şikayet sayısı
    assigned_unit: Optional[str]   # Eşleşen belediye birimi
    status: str                    # İşlem durumu