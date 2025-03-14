import streamlit as st
import pandas as pd
import plotly.express as px  # Para gráficos interativos

# Configuração da página
st.set_page_config(page_title="Despesas UFCAT", page_icon="💰", layout="centered")

# Cabeçalho
st.image("https://ufcat.edu.br/_nuxt/img/UFCAT%20-%20Logo%20%20Header.96f163c.png", use_container_width=True)  # Substitua por uma imagem real
st.title("💰 Interface de Despesas da UFCAT")
st.markdown("""
    **Escolha o ano desejado e explore as despesas da UFCAT.**
    Utilize a barra lateral para selecionar o ano e os parâmetros do gráfico.
    Desça a pagina que chegara ao gráfico.
""")
st.divider()

# Sidebar
with st.sidebar:
    st.title("⚙️ Configurações")
    st.markdown("Selecione o ano para visualizar as despesas:")
    ANO = st.number_input("Ano", min_value=2015, max_value=2025, value=2023)
    
    # Seletor de colunas para o gráfico
    st.markdown("---")
    st.markdown("**Configurações do Gráfico**")

# Função para carregar dados com cache
@st.cache_data
def carregar_dados(file_path):
    return pd.read_excel(file_path)

# Mapeamento de anos para arquivos
file_mapping = {
    2015: "DADOS_UFCAT/UFCAT_2015_DESPESAS.xlsx",
    2016: "DADOS_UFCAT/UFCAT_2016_DESPESAS.xlsx",
    2017: "DADOS_UFCAT/UFCAT_2017_DESPESAS.xlsx",
    2018: "DADOS_UFCAT/UFCAT_2018_DESPESAS.xlsx",
    2019: "DADOS_UFCAT/UFCAT_2019_DESPESAS.xlsx",
    2020: "DADOS_UFCAT/UFCAT_2020_DESPESAS.xlsx",
    2021: "DADOS_UFCAT/UFCAT_2021_DESPESAS.xlsx",
    2022: "DADOS_UFCAT/UFCAT_2022_DESPESAS.xlsx",
    2023: "DADOS_UFCAT/UFCAT_2023_DESPESAS.xlsx",
    2024: "DADOS_UFCAT/UFCAT_2024_DESPESAS.xlsx",
    2025: "DADOS_UFCAT/UFCAT_2025_DESPESAS.xlsx",
}

# Carregar dados
if ANO in file_mapping:
    df_dados = carregar_dados(file_mapping[ANO])
    
    # Atualizar as opções do seletor de colunas
    colunas_disponiveis = df_dados.columns.tolist()
    with st.sidebar:
        coluna_x = st.selectbox("Selecione a coluna para o eixo X:", colunas_disponiveis, index=colunas_disponiveis.index("NOME GRUPO DE DESPESA") if "NOME GRUPO DE DESPESA" in colunas_disponiveis else 0)
        coluna_y = st.selectbox("Selecione a coluna para o eixo Y:", colunas_disponiveis, index=colunas_disponiveis.index("ORCAMENTO REALIZADO") if "ORCAMENTO REALIZADO" in colunas_disponiveis else 1)
        st.markdown("Desenvolvido por JOAO")
else:
    st.error("Arquivo não encontrado para o ano selecionado.")
    st.stop()

# Exibir métricas resumidas
st.subheader("📊 Métricas Resumidas")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Despesas", f"R$ {df_dados['ORCAMENTO REALIZADO'].sum():,.2f}")
with col2:
    st.metric("Média de Despesas", f"R$ {df_dados['ORCAMENTO REALIZADO'].mean():,.2f}")
with col3:
    st.metric("Número de Registros", len(df_dados))

# Gráfico de despesas
st.subheader("📈 Gráfico de Despesas")
# Usando uma coluna existente, como "NOME GRUPO DE DESPESA" ou "NOME CATEGORIA ECONOMICA"
lab = px.bar(
    df_dados,
    x="NOME GRUPO DE DESPESA",  # Substitua por uma coluna válida
    y="ORCAMENTO REALIZADO",
    title=f"Despesas por Grupo de Despesa em {ANO}"
)
st.plotly_chart(lab, use_container_width=True)

st.subheader("📈 Gráfico atualizavel")
if coluna_x and coluna_y:
    fig = px.bar(
        df_dados,
        x=coluna_x,
        y=coluna_y,
        title=f"Despesas por {coluna_x} em {ANO}"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Selecione as colunas para os eixos X e Y na barra lateral.")

# Tabela de dados
st.subheader("📋 Tabela de Dados")
st.dataframe(
    df_dados,
    column_config={
        "ORCAMENTO REALIZADO": st.column_config.NumberColumn("Total (R$)", format="R$ %.2f"),
    },
    use_container_width=True,
)

# Rodapé
st.divider()
st.markdown("Feito por João Paulo Machado Lopes")