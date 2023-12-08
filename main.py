import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
@st.cache_data
def load_database():
  return pd.read_parquet('brasil_estados.parquet'), pd.read_parquet('SSEuropa.parquet')

estados, europa = load_database()

st.dataframe(estados)

st.dataframe(europa)

st.table(estados)
