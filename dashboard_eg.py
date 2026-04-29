import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# 1. Configuração da página
st.set_page_config(page_title="Dashboard EG Alimentos", layout="wide")

# 2. Função para carregar dados (com cache para performance)
@st.cache_data
def carregar_dados():
    # Busca as credenciais de forma segura
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    driver = os.getenv('DB_DRIVER')
    
    # Monta a string de conexão sem expor os dados no código
    connection_string = f'mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}'
    engine = create_engine(connection_string)
    
    query = """SELECT * FROM VW_VENDAS"""
    df = pd.read_sql(query, engine)
    
    # Criando colunas de tempo para os filtros
    df['DATAHORA'] = pd.to_datetime(df['DATAHORA'], dayfirst=True, errors='coerce')
    df['ANO_MES'] = df['DATAHORA'].dt.strftime('%Y-%m')   
    df['ANO'] = df['DATAHORA'].dt.year
    df['MES'] = df['DATAHORA'].dt.month_name()
    df['DIA'] = df['DATAHORA'].dt.date
    return df

df_raw = carregar_dados()

# 3. Barra Lateral (Filtros)
st.sidebar.header("Filtros Estratégicos")

anos = st.sidebar.multiselect("Ano", options=df_raw["ANO"].unique(), default=df_raw["ANO"].unique())
meses = st.sidebar.multiselect("Mês", options=df_raw["MES"].unique(), default=df_raw["MES"].unique())
pagamentos = st.sidebar.multiselect("Forma de Pagamento", options=df_raw["FORMA_PGTO"].unique(), default=df_raw["FORMA_PGTO"].unique())
vendedores = st.sidebar.multiselect("Vendedores", options=df_raw["VENDEDOR"].unique(), default=df_raw["VENDEDOR"].unique())

# Aplicando os filtros ao DataFrame
df_filtrado = df_raw[
    (df_raw["VENDEDOR"].isin(vendedores)) &
    (df_raw["FORMA_PGTO"].isin(pagamentos)) &
    (df_raw["ANO"].isin(anos)) &
    (df_raw["MES"].isin(meses))
]

# 4. Título Principal
st.title("📊 Gestão de Vendas - EG Alimentos")
st.markdown("---")

# 5. Métricas de Resumo (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Faturamento Total", f"R$ {df_filtrado['TOTAL_VENDA'].sum():,.2f}")
col2.metric("Qtd. Vendas", df_filtrado.shape[0])
col3.metric("Ticket Médio", f"R$ {df_filtrado['TOTAL_VENDA'].mean():,.2f}")

st.markdown("---")

# 6. Gráficos Interativos
tab1, tab2, tab3 = st.tabs(["Vendas por Dia", "Vendas por Mês", "Meios de Pagamento"])

with tab1:
    vendas_dia = df_filtrado.groupby("DIA")["TOTAL_VENDA"].sum().reset_index()
    fig_dia = px.line(vendas_dia, x="DIA", y="TOTAL_VENDA", title="Evolução Diária de Vendas")
    st.plotly_chart(fig_dia, use_container_width=True)

with tab2:
    vendas_mes = df_filtrado.groupby("MES")["TOTAL_VENDA"].sum().reset_index()
    fig_mes = px.bar(vendas_mes, x="MES", y="TOTAL_VENDA", title="Faturamento Mensal", color_discrete_sequence=['#003366'])
    st.plotly_chart(fig_mes, use_container_width=True)

    vendas_periodo = df_filtrado.groupby("ANO_MES")["TOTAL_VENDA"].sum().reset_index()
    fig_periodo = px.line(vendas_periodo, x="ANO_MES", y="TOTAL_VENDA", title="Evolução de Faturamento (Ano/Mês)", markers=True)
    fig_periodo.update_traces(line_color='#06232e') 
    st.plotly_chart(fig_periodo, use_container_width=True)

with tab3:
    vendas_pgto = df_filtrado.groupby("FORMA_PGTO")["TOTAL_VENDA"].sum().reset_index()
    fig_pgto = px.pie(vendas_pgto, values="TOTAL_VENDA", names="FORMA_PGTO", title="Distribuição por Pagamento", hole=0.4)
    st.plotly_chart(fig_pgto, use_container_width=True)