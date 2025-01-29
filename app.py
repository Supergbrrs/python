import time
import datetime
import requests
import re
import streamlit as st

############# SALDO SMS ####################

# URL da API que você deseja consumir
api_url = "https://api.ctxtelle.com.br/balance"

# Cabeçalhos da requisição (se necessário)
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 523e69709c287165ab02cd518f6216e3aff2cb25"  # Exemplo de envio de token
}

# Título do aplicativo Streamlit
st.title("Consulta de Saldo SMS")

try:
    # Faz a requisição GET
    response = requests.get(api_url, headers=headers)

    # Verifica o status da resposta
    response.raise_for_status()

    # Converte a resposta para JSON
    dados = response.json()
        
    # Extrair o saldo do dicionário
    saldo = dados['detail']['saldo']
    
    # Formatar o saldo no formato desejado
    saldo_formatado = f"Saldo: R$ {saldo}"

    # Exibir o resultado no Streamlit
    st.success(saldo_formatado)

except requests.exceptions.RequestException as e:
    st.error(f"Erro na requisição: {e}")

# Exibir a hora da consulta
data_hora_atual = datetime.datetime.now()
data_hora_formatada = data_hora_atual.strftime("%H:%M:%S")

st.write("#### SALDO ROTA ####")
st.write("*SMS*")
st.write(saldo_formatado)
st.write("*Hora da Consulta:*", data_hora_formatada)
