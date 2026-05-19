"🏛️ Mavi Masa AI"

Belediye Akıllı Şikayet Triaj ve Yönlendirme Sistemi 

Mavi Masa AI, belediyelere gelen vatandaş şikayetlerini doğal dil işleme (NLP) ile anlayan, aciliyet sırasına koyan, konumlandıran ve doğru birime otomatik yönlendiren Agentic (Otonom Ajan) tabanlı bir yapay zeka asistanıdır.

BTK 2026 Hackathon kapsamında geliştirilmiştir.

"🚀 Neden Mavi Masa AI? (Problem ve Çözüm)"

Büyükşehir belediyelerinde her gün binlerce çağrı ve mesaj manuel olarak operatörler tarafından okunup ilgili birimlere atanmaya çalışılmaktadır. Bu durum "ambulans/göçük" gibi acil durumların önemsiz şikayetlerin arkasında beklemesine ve kronikleşen bölgesel sorunların (aynı çukuru 50 kişinin şikayet etmesi) gözden kaçmasına neden olmaktadır.

Çözümümüz: Gelen metni saniyeler içinde analiz eden, aciliyet skoru (1-10) üreten ve LangGraph destekli 4 farklı otonom ajan ile süreci uçtan uca yöneten akıllı bir sistem.

"✨ Temel Özellikler (İnovasyon Noktaları)"
🧠 Agentic Mimari (LangGraph): Şikayetler tek bir model yerine; Anlama, Konumlandırma, Kümeleme ve Yönlendirme görevlerinde uzmanlaşmış bir ajan zincirinden geçer.

🚨 Dinamik Aciliyet Skoru: "Sokak lambası yanmıyor" (Skor: 2) ile "Kanalizasyon patladı" (Skor: 9) şikayetleri ayrıştırılarak birimlere öncelik sırasıyla iletilir.

🗺️ Akıllı Kümeleme Motoru (pgvector): Şikayetler HuggingFace modelleriyle vektör uzayına dönüştürülür. Kosinüs benzerliği algoritmaları kullanılarak "Bu mahallede aynı çukuru 47 kişi daha şikayet etti" tespiti yapılır ve belediyeye bölgesel kriz haritası sunulur.

"🛠️ Teknoloji Yığını (Tech Stack)"
Zeka Çekirdeği (Backend)
* Çerçeve: FastAPI, Python

* LLM Motoru: Google Gemini 2.5 Flash (Hız ve yapılandırılmış veri analizi için)

* Vektör Modeli: HuggingFace all-MiniLM-L6-v2 (Yerel, yüksek performanslı embedding)

* Orkestrasyon: LangGraph

Veri 
* Veritabanı: Supabase (PostgreSQL) + pgvector eklentisi



