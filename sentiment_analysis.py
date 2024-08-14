import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Model ve Tokenizer'ı yükleme
model = load_model('entity_sentiment_model.h5')

# Tokenizer'ı yükleme (Eğitim sırasında kaydedildiğini varsayıyoruz)
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

def predict_sentiment(model, tokenizer, text):
    """
    Verilen metin için sentiment tahmini yapar.

    Args:
        model (keras.Model): Eğitimli sentiment analizi modeli.
        tokenizer (Tokenizer): Eğitim sırasında kullanılan Tokenizer.
        text (str): Sentiment analizi yapılacak metin.

    Returns:
        str: Tahmin edilen sentiment (olumlu, olumsuz, nötr).
    """
    # Metni tokenize et ve pad işlemi yap
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=100, padding='post')
    
    # Model tahmini yap
    prediction = model.predict(padded_sequences)
    
    # Tahmin edilen sınıfı bul
    sentiment_index = prediction.argmax(axis=1)[0]  # Sınıf endeksini alın
    
    # Endeksleri etiketlere dönüştür
    sentiment_label = 'nötr'  # Varsayılan nötr
    if sentiment_index == 0:
        sentiment_label = 'olumsuz'
    elif sentiment_index == 1:
        sentiment_label = 'olumlu'
    
    return sentiment_label

def analyze_sentiments(df):
    """
    DataFrame'deki yorumları sentiment analizinden geçirir.

    Args:
        df (pd.DataFrame): Yorumları içeren DataFrame.

    Returns:
        pd.DataFrame: Sentiment sonuçları ile güncellenmiş DataFrame.
    """
    sentiments = []
    
    for index, row in df.iterrows():
        comment = row['comment']  # Yorumun bulunduğu sütun adı 'comment'
        
        # Sentiment analizini gerçekleştir
        sentiment = predict_sentiment(model, tokenizer, comment)
        
        sentiments.append(sentiment)
    
    # Yeni sentiment sütununu ekleme
    df['sentiment'] = sentiments
    
    return df
