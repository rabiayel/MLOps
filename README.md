# MLOps

Makine öğrenmesi modellerinin eğitimden web tabanlı dağıtıma (deployment) kadar uçtan uca yaşam döngüsünü gösteren MLOps uygulama koleksiyonu. Flask ile model servisleştirme, çoklu veri kaynağı işleme ve farklı uygulama versiyonlarını kapsar.

---

## İçerik

### 📓 MLOps.ipynb
Model eğitimi, veri işleme ve dağıtıma hazırlık adımlarını kapsayan ana notebook. Maaş tahmini gibi regresyon problemleri üzerinde model geliştirme ve serileştirme (`pickle`) süreçlerini içerir.

---

### 🚀 Flask Uygulamaları (app.py – app5.py)
Eğitilmiş modelin web servisi olarak dağıtımını gösteren **Flask** tabanlı uygulamalar. Her dosya, dağıtım sürecinin farklı bir aşamasını veya iterasyonunu temsil eder:

| Dosya | Açıklama |
|---|---|
| `app.py` | Temel Flask uygulaması — `maas.pkl` modelini yükler, `/predict` endpoint'i ile tecrübe, yazılı sınav ve mülakat puanlarına göre maaş tahmini döner |
| `app1.py` – `app5.py` | Aynı modelin farklı geliştirme/iterasyon aşamaları — form işleme, hata yönetimi, ek endpoint'ler veya arayüz geliştirmeleri |

**Mimari:**
- Model yükleme: `pickle` ile `maas.pkl`
- Web framework: Flask (`render_template`, `request`, route'lar)
- Giriş: Kullanıcıdan alınan form verileri (tecrübe, yazılı, mülakat puanı)
- Çıkış: HTML şablon üzerinden tahmin sonucu

- **Klasör:** `templates/` — Flask için HTML arayüz şablonları

---

## Veri Setleri ve Dosyalar

| Dosya | Açıklama |
|---|---|
| `maas.pkl` | Eğitilmiş maaş tahmin modeli (serileştirilmiş) |
| `hiring.csv`, `hr_data.csv` | İnsan kaynakları / işe alım verileri |
| `iris.csv` | Klasik Iris çiçek sınıflandırma veri seti |
| `cars.xls` | Otomotiv verisi |
| `lang_data.csv`, `prog_languages_data.csv` | Programlama dili verileri |
| `data.zip` | Arşivlenmiş veri koleksiyonu |
| `image_01.jpg`–`image_03.jpg` | Örnek görseller |
| `song.mp3`, `secret_of_success.mp4` | Ses ve video örnek dosyaları |
| `my_example.pdf`, `my_example.docx` | Örnek belge dosyaları |
| `example_text.txt` | Örnek metin dosyası |

---

## Kullanılan Teknolojiler

- Python 3
- Jupyter Notebook
- Flask
- pickle (model serileştirme)
- HTML (Flask şablonları)
- pandas, scikit-learn (muhtemel model eğitimi)

---

## Başlarken

```bash
git clone https://github.com/rabiayel/MLOps.git
cd MLOps
pip install flask pandas scikit-learn
python app.py
```

Uygulama ayağa kalktıktan sonra tarayıcıda `http://127.0.0.1:5000` adresine giderek tahmin formunu kullanabilirsin.

---

## Proje Amacı

Bu repo, bir makine öğrenmesi modelinin nasıl eğitilip serileştirileceğini ve ardından bir web uygulaması (Flask) üzerinden kullanıcıya nasıl sunulacağını adım adım göstererek **MLOps temel prensiplerini** (eğitim → serileştirme → dağıtım) uygulamalı olarak öğretmeyi amaçlamaktadır.
