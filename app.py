import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Carrega as variáveis do arquivo .env
load_dotenv()

# 1. CONFIGURAÇÃO DA PÁGINA (Aba do Navegador)
st.set_page_config(
    page_title="SaborTech - Dashboard Logístico",
    page_icon="🚚",
    layout="wide"
)

# 2. CONEXÃO COM O BANCO DE DADOS (MySQL)
# As credenciais são lidas do arquivo .env — nunca hardcoded!
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "logistica_alimentar")

try:
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
except Exception as e:
    st.error(f"Erro ao configurar o motor do banco de dados: {e}")

# 3. FUNÇÃO PARA CARREGAR DADOS
def carregar_dados():
    query = """
    SELECT 
        f.nome AS Fornecedor, 
        n.numero_nota AS 'Nº Nota', 
        n.valor_total AS 'Valor (R$)', 
        n.data_emissao AS 'Data Emissão'
    FROM notas_fiscais n
    JOIN fornecedores f ON n.fornecedor_id = f.id
    """
    return pd.read_sql(query, engine)

# --- INTERFACE DO DASHBOARD ---

st.title("🚚 Dashboard de Recebimento | SaborTech Alimentos")
st.markdown("Monitoramento estratégico de Notas Fiscais e Fluxo de Suprimentos.")
st.divider()

try:
    df = carregar_dados()

    # 4. INDICADORES (KPIs) NO TOPO
    col1, col2, col3 = st.columns(3)

    total_notas = len(df)
    valor_total = df['Valor (R$)'].sum()
    media_nota = df['Valor (R$)'].mean() if total_notas > 0 else 0

    col1.metric("Total de Notas Processadas", total_notas)
    col2.metric("Volume Financeiro Total", f"R$ {valor_total:,.2f}")
    col3.metric("Ticket Médio por Nota", f"R$ {media_nota:,.2f}")

    st.markdown("###")

    # 5. GRÁFICOS E TABELAS
    col_grafico, col_tabela = st.columns([2, 1])

    with col_grafico:
        st.subheader("Análise de Volume por Fornecedor")
        chart_data = df.groupby('Fornecedor')['Valor (R$)'].sum().sort_values(ascending=False)
        st.bar_chart(chart_data)

    with col_tabela:
        st.subheader("Últimos Lançamentos")
        st.dataframe(df, hide_index=True, use_container_width=True)

    # 6. RODAPÉ TÉCNICO
    st.divider()
    st.caption("🚀 Projeto de Portfólio: Sistema de Monitoramento Logístico Integrado (SQL + Python)")

except Exception as e:
    st.error("⚠️ Não foi possível carregar os dados.")
    st.info("Dica: Verifique se você criou o banco 'logistica_alimentar' no MySQL, configurou o .env e inseriu os dados.")
    st.expander("Ver detalhes do erro").write(e)
