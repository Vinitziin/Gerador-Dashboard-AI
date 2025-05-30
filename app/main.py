import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Gerador de Dashboard", layout="wide")

st.title("📊 Gerador de Dashboards via Prompt")

st.markdown("Envei um arquivo 'CSV' e descreva o que você deseja vizualizar.")

# Upload CSV file
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Arquivo carregado com sucesso!")
        st.subheader("Pré-visualização dos dados:")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"❌ Erro ao carregar o arquivo: {e}")