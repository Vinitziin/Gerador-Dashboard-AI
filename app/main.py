import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.llm_handler import gerar_codigo
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gerador de Dashboard", layout="wide")

st.title("📊 Gerador de Dashboards via Prompt")

st.markdown("Envie um arquivo 'CSV' e descreva o que você deseja vizualizar.")

#Subir o arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Arquivo carregado com sucesso!")
        st.subheader("Pré-visualização dos dados:")
        st.dataframe(df.head())

        prompt = prompt = st.text_input("📢 Descreva o que deseja visualizar (ex: quero ver a média semanal)")
        
        if prompt and uploaded_file is not None:
            with st.spinner("Gerando código..."):
                codigo_gerado = gerar_codigo(
                    f"DataFrame com colunas: {', '.join(df.columns)}.\nUsuário pediu: {prompt}\nGere um código Python para isso."
                )
                st.subheader("🧠 Código Gerado:")
                st.code(codigo_gerado, language='python')
    except Exception as e:
        st.error(f"❌ Erro ao carregar o arquivo: {e}")