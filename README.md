# BetaVerse_TTDI_Senaryosu

![Takım Id 562234](https://github.com/user-attachments/assets/0eb1861f-71bb-40ab-b5ea-4d1d3de0dff4)

 
 ## Üyeler
 
•Merve Zeyep Tiryaki 
•Elif Şevval Kam
•Zeynep Öztek 
•Dr.Erman Zurnacı(Danışman)
•Dr.Merve Ayyüce Kızrak(Mentor) 
 
 ## Üyelerin Görevleri
 
 ***E.Şevval Kam***
•Veri Etiketleme: Verilerin doğru ve tutarlı bir şekilde etiketlenmesi, modelin doğru öğrenmesi için önemlidir.
•Araştırma: Alanla ilgili literatür taraması yaparak güncel bilgi ve yöntemleri takip etme.
•Grafik Tasarımı: Bilgi ve verilerin görsel olarak çekici ve anlaşılır bir şekilde sunulması için grafikler ve görsellerin tasarlanması.

***M.Zeynep Tiryaki***
•Dokümantasyon: Çalışmaların, yöntemlerin ve sonuçların detaylı bir şekilde yazılması ve düzenlenmesi.
•Sunum: Proje bulgularının, sonuçlarının ve gelişmelerinin etkili bir şekilde sunulması ve paylaşılması.
•Veri Etiketleme: Verilerin doğru ve tutarlı bir şekilde etiketlenmesi, modelin doğru öğrenmesi için önemlidir.

***Zeynep Öztek***
•Model Geliştirme: Makine öğrenmesi veya yapay zeka modellerinin tasarlanması, eğitilmesi ve optimize edilmesi.
•Kod Yazma: Geliştirilen modellerin ve algoritmaların yazılım kodlarının yazılması ve test edilmesi.

# Text Classification and Named Entity Recognition (NER) API

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://betaverse.streamlit.app/)

Bu proje, kullanıcıların yorumları sentiment analizine tabi tutarak sonuçları çeşitli formatlarda indirmelerine olanak tanıyan bir Streamlit uygulamasıdır. Uygulama, bir CSV veya Excel dosyasını yükleyerek yorumları analiz eder ve sonuçları PDF veya DOCX formatında indirmeyi sağlar.

## İçindekiler

- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Fonksiyonlar](#fonksiyonlar)
- [Dosya Formatları](#dosya-formatları)

## Gereksinimler

Bu uygulamanın çalışması için aşağıdaki Python kütüphanelerinin kurulu olması gerekmektedir:

- `streamlit`
- `pandas`
- `tensorflow`
- `openpyxl`
- `fpdf`
- `python-docx`

Bu kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install streamlit pandas tensorflow openpyxl fpdf python-docx
   ```
## Kurulum

1. **Model ve Tokenizer'ı Yükleyin:**
   - `entity_sentiment_model.h5` dosyasını ve `tokenizer.pkl` dosyasını proje dizinine yerleştirin.

2. **Kodları Çalıştırın:**
   - Proje dizininde terminal veya komut satırında şu komutu çalıştırarak Streamlit uygulamasını başlatın:

     ```bash
     streamlit run app.py
     ```

## Kullanım

1. **Dosya Yükleyin:**
   - Uygulama açıldığında, "Dosya yükleyin (CSV, Excel)" düğmesini kullanarak analiz etmek istediğiniz CSV veya Excel dosyasını yükleyin.

2. **Analiz Sonuçlarını Görüntüleyin:**
   - Yüklenen dosyadaki yorumlar analiz edildikten sonra sonuçlar ekranda gösterilecektir.

3. **Sonuçları İndirin:**
   - Analiz sonuçlarını PDF veya DOCX formatında indirmek için ilgili düğmeleri kullanın.

## Fonksiyonlar

- **`predict_sentiment(model, tokenizer, text)`**: Verilen metin için sentiment tahmini yapar.
- **`analyze_sentiments(df)`**: DataFrame'deki yorumları sentiment analizine tabi tutar ve sonuçları içeren yeni bir sütun ekler.
- **`dataframe_to_pdf(df, output_buffer)`**: Bir DataFrame'i PDF formatına dönüştürür ve belirtilen buffer'a kaydeder.
- **`dataframe_to_docx(df, output_buffer)`**: Bir DataFrame'i DOCX formatına dönüştürür ve belirtilen buffer'a kaydeder.

## Dosya Formatları

- **CSV:** Yorumlar `comment` sütununda yer almalıdır.
- **Excel:** Yorumlar `comment` sütununda yer almalıdır.
