import streamlit as st
import pandas as pd

st.set_page_config(page_title="PROJETOS DENTRO DA UFCAT", page_icon=":mortar_board:", layout="centered")

st.image("https://ufcat.edu.br/_nuxt/img/UFCAT%20-%20Logo%20%20Header.96f163c.png", width=100)
st.title(":mortar_board: Interface Projetos da UFCAT")
st.markdown("""
    **Escolha a área desejada e explore os projetos da UFCAT.**
    Utilize a barra lateral para selecionar sua área de interesse.
    Temos duas tebelas de dados diferentes, observe a sua legenda.
    Desça a página para visualizar o gráfico.
""")
st.divider()

@st.cache_data
def carregar_dados():
    return pd.read_excel('DADOS_FILTRADOS/UFCAT_nodinero.xlsx')
def carregar_dados1():
    return pd.read_excel('DADOS_FILTRADOS/UFCAT_dinero.xlsx')
df_dados = carregar_dados()
df_dados1 = carregar_dados1()

with st.sidebar:
    st.title("⚙️ Configurações")
    st.markdown("**Selecione o instituto que deseja ver todos os projetos que estão em andamento:**")

    unidades_disponiveis = df_dados["UNIDADE"].unique()
    unidades_selecionadas = st.multiselect(
        "Selecione as unidades para exibir:",
        options=unidades_disponiveis,
        default=None
    )

with st.sidebar:
    st.markdown("**Selecione o instituto que deseja ver os projetos com bolsas que estão em andamento:**")

    unidades_disponiveis1 = df_dados1["UNIDADE"].unique()
    unidades_selecionadas1 = st.multiselect(
        "Selecione as unidades para exibir:",
        options=unidades_disponiveis1,
        default=None
    )
    st.markdown("---")

df_filtrado = df_dados[df_dados["UNIDADE"].isin(unidades_selecionadas)]
df_filtrado1 = df_dados1[df_dados1["UNIDADE"].isin(unidades_selecionadas1)]

st.subheader("📋 Tabela de Todos os Projetos Em Andamento Na Ufcat.")
st.markdown(f"**Exibindo dados para {len(df_dados)} projetos.**")

st.dataframe(
    df_dados,
    use_container_width=True,
)

st.subheader("📋 Tabela de Todos os Projetos com bolsas Em Andamento Na Ufcat.")
st.markdown(f"**Exibindo dados para {len(df_dados1)} projetos.**")

st.dataframe(
    df_dados1,
    use_container_width=True,
)

st.subheader("Tabelas Interativas, Escolha Seus Dados Na Barra Lateral.")
st.markdown(f"**Exibição de tabelas:**")

st.subheader("📋 Tabela de Projetos de sua instituições escolhidas.")
st.markdown(f"**Exibindo dados para {len(df_filtrado)} projetos.**")
st.dataframe(
    df_filtrado,
    use_container_width=True,
)

st.subheader("📋 Tabela de Projetos com bolsas de sua instituições escolhidas.")
st.markdown(f"**Exibindo dados para {len(df_filtrado1)} projetos.**")
st.dataframe(
    df_filtrado1,
    use_container_width=True,
)

st.divider()
st.markdown("Feito por João Paulo Machado Lopes")