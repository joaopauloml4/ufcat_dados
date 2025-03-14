import streamlit as st
import pandas as pd


st.divider()
st.title("INTERFACE PARA DESPESAS DA UFCAT:")
st.title("ESCOLHA O ANO QUE DESEJE E DESCUBRA.")
ANO = st.sidebar.number_input("ANO", min_value=2015, max_value=2025, value=2015)
st.divider()
print(ANO)
ANO = ana
@st.cache_data
def carregar_dados(UFCAT):
    Tab = pd.read_excel(UFCAT)
    print(Tab)
    return Tab

if ANO == 2015:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2015_DESPESAS.xlsx")
if ANO == 2016:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2016_DESPESAS.xlsx")
if ANO == 2017:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2017_DESPESAS.xlsx")
if ANO == 2018:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2018_DESPESAS.xlsx")
if ANO == 2019:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2019_DESPESAS.xlsx")
if ANO == 2020:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2020_DESPESAS.xlsx")
if ANO == 2021:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2021_DESPESAS.xlsx")
if ANO == 2022:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2022_DESPESAS.xlsx")
if ANO == 2023:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2023_DESPESAS.xlsx")
if ANO == 2024:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2024_DESPESAS.xlsx")
if ANO == 2025:
    df_dados = carregar_dados("DADOS_UFCAT/UFCAT_2025_DESPESAS.xlsx")

config = {
    "_index": st.column_config.NumberColumn("year", format=ANO),
    "ORCAMENTO REALIZADO": st.column_config.NumberColumn("Total ($)"),
}

st.dataframe(df_dados, column_config=config)
print(df_dados)
