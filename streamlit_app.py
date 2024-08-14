import streamlit as st
import pandas as pd
from sentiment_analysis import analyze_sentiments
from file_processor import dataframe_to_pdf, dataframe_to_docx
from io import BytesIO

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Sentiment Analysis Dashboard',
    page_icon=':bar_chart:',  # Bu bir emoji kısa kodu, bir URL de olabilir.
)

# -----------------------------------------------------------------------------
# Başlık
st.title('Sentiment Analysis Dashboard')

# Dosya yükleme
uploaded_file = st.file_uploader("Dosya yükleyin (CSV, Excel)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        # Dosya tipi belirleme ve okuma
        if uploaded_file.name.endswith('.csv'):
            # CSV dosyasını UTF-8 kodlamasıyla oku
            df = pd.read_csv(uploaded_file, encoding='utf-8')
        elif uploaded_file.name.endswith('.xlsx'):
            # Excel dosyasını oku
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Desteklenmeyen dosya formatı.")
            df = None

        if df is not None and 'comment' in df.columns:
            # Sentiment analizi yap
            analyzed_df = analyze_sentiments(df)

            # Sonuçları gösterme
            st.header('Analiz Sonuçları')
            st.dataframe(analyzed_df)

            # PDF olarak indirme
            pdf_buffer = BytesIO()
            dataframe_to_pdf(analyzed_df, pdf_buffer)
            pdf_buffer.seek(0)
            st.download_button(
                label="PDF olarak indir",
                data=pdf_buffer,
                file_name="sentiment_analysis_results.pdf",
                mime="application/pdf"
            )

            # DOCX olarak indirme
            docx_buffer = BytesIO()
            dataframe_to_docx(analyzed_df, docx_buffer)
            docx_buffer.seek(0)
            st.download_button(
                label="DOCX olarak indir",
                data=docx_buffer,
                file_name="sentiment_analysis_results.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

        else:
            st.error("DataFrame'de 'comment' adında bir sütun bulunamadı. Lütfen 'comment' sütununu içeren bir dosya yükleyin.")
    except Exception as e:
        st.error(f"Bir hata oluştu: {str(e)}")
else:
    st.write("Lütfen bir dosya yükleyin.")
