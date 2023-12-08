import streamlit as st
import pandas as pd

@st.cache_data
def load_database():
  return pd.read_excel('brasil_estados.xlsx'), pd.read_parquet('SSEuropa.parquet)

estados, europa = load_database()

st.dataframe(estados)

st.dataframe(europa)                                                             
