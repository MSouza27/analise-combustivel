import pandas as pd
import openpyxl
import streamlit as st
import altair as alt
from PIL import Image

@st.cache_data
def gerar_data():
    df = pd.read_excel(
        io="database_anp.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        usecols="A:Q",
        skiprows=6,
        header=6,
        nrows=400000
    )
    return df
df = gerar_data()

colunas_uteis = ['MÊS', 'PRODUTO', 'REGIÃO','ESTADO', 'PRECO MÉDIO REVENDA']
df = df[colunas_uteis]

df = df.dropna(subset=['PRECO MÉDIO REVENDA'], how='any')


with st.sidebar:
    st.subheader('Analise Combustivel')
    #logo_teste = Image.open('')
    #st.image(logo_teste, use_column_width=True)
    fProduto = st.selectbox(
        "Selecione o combustivel:",
        options=df['PRODUTO'].unique()
    )

    fEstado = st.selectbox(
        "Selecione o estado:",
        options=df['ESTADO'].unique()
    )

    df['MÊS'] = pd.to_datetime(df['MÊS'], errors='coerce')
    df['ANO'] = df['MÊS'].dt.year
    df = df.dropna(subset=['ANO'], how='any')
    df['ANO'] = df['ANO'].fillna(0).astype(int)


    fAno = st.multiselect(
        "Selecione o(s) ano(s):",
        options=df['ANO'].sort_values().unique(),
        default=df['ANO'].max()
    )

    dados_usuario = df.loc[(
        df['PRODUTO'] == fProduto) &
        (df['ESTADO'] == fEstado) &
        (df['ANO'].isin(fAno))
    ]



dados_usuario['MÊS'] = pd.to_datetime(dados_usuario['MÊS'], errors='coerce')
updateDatas = dados_usuario['MÊS'].dt.strftime('%Y/%b')
dados_usuario['MÊS'] = updateDatas[0:]

st.header('Evolução dos Preços de Combustíveis')
st.markdown('**Combustível selecionado**: ' + fProduto)
st.markdown('**Estado**: ' + fEstado)

graf_comb_estado = (
    alt.Chart(dados_usuario)
    .mark_line(point=True)
    .encode(
        x=alt.X('month(MÊS):O', title='Mês'),
        y=alt.Y('mean(PRECO MÉDIO REVENDA):Q', title='Preço médio de revenda (R$/L)'),
        color=alt.Color('ANO:N', title='Ano'),
        tooltip=['ANO', 'MÊS', 'PRECO MÉDIO REVENDA']
    )
    .properties(
        width=800,
        height=400,
        title=f"Evolução anual do preço médio - {fProduto} ({fEstado})"
    )
)


st.altair_chart(graf_comb_estado)
