import streamlit as st
import pandas as pd

# Configurar a página para tela cheia
st.set_page_config(layout="wide")

# Adicionar o logo da empresa
#logo_path = "C:/Users/Gustavo/Desktop/Saldo/logo.png"  # Altere para o caminho correto da imagem

# Layout com colunas para centralizar o logo
#col1, col2, col3 = st.columns([1, 3, 1])

#with col2:
#    st.image(logo_path, width=200)  # Ajuste o tamanho conforme necessário

# Adicionar CSS global para centralizar e aumentar o tamanho do título
st.markdown(
    """
    <style>
        .title-container {
            text-align: center;
            margin-bottom: 1px;
        }
        .title {
            font-size: 50px !important;
            font-weight: bold;
            color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Exibir o título centralizado e com fonte maior
st.markdown('<div class="title-container"><h1 class="title">📊 CONTROLE DE SALDOS ROTAS</h1></div>', unsafe_allow_html=True)

# Caminho do arquivo Excel
file_path = r"saldo_telecom.xlsx"

try:
    # Ler o arquivo Excel
    xls = pd.ExcelFile(file_path)

    # Pegar a primeira aba automaticamente
    first_sheet = xls.sheet_names[1]

    # Carregar os dados da primeira aba
    df = pd.read_excel(xls, sheet_name=first_sheet)

    # Exibir a planilha com largura total
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error(f"Arquivo não encontrado: {file_path}")

except Exception as e:
    st.error(f"Ocorreu um erro: {e}")
