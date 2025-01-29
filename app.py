import time
import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit as st

# Título do aplicativo Streamlit
st.title("Consulta de Saldos e Consumos")

# Inicializar o driver do Chrome
driver = webdriver.Chrome()
driver.execute_cdp_cmd('Storage.clearDataForOrigin', {
    "origin": '*',
    "storageTypes": 'all',
})

##### Saldo BFT #########

# URL de login
login_url = "https://sistemas.bfttelecom.com.br/application/login"

# Abrir a página de login
driver.get(login_url)

# Aguardar até que o campo de usuário esteja visível e interagível
username_field = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "user_acess"))
)

# Preencher o campo de usuário
username_field.send_keys("cristanotobia2022@gmail.com")

# Aguardar até que o campo de senha esteja visível e interagível
password_field = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "pass_acess"))
)

# Preencher o campo de senha
password_field.send_keys("Tobia1978")

# Enviar o formulário de login
password_field.submit()

# Aguardar redirecionamento após o login
time.sleep(10)

# Armazenar o valor do elemento em uma variável
gasto_element = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.green'))
)
saldo_BFT = gasto_element.text

############# SALDO TELGlobe ##########################

# URL de login
login_url = "https://177.136.226.7/security/login"

# Abrir a página de login
driver.get(login_url)

# Localizar o elemento hover de relatórios
hover_element = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='details-button']"))
)

# Clicar no elemento hover
hover_element.click()

# Localizar o elemento hover de relatórios
hover_element = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='proceed-link']"))
)

# Clicar no elemento hover
hover_element.click()

# Aguardar até que o campo de usuário esteja visível e interagível
username_field = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.ID, "username"))
)

# Preencher o campo de usuário
username_field.send_keys("wntelecom2")

# Aguardar até que o campo de senha esteja visível e interagível
password_field = WebDriverWait(driver, 3).until(
   EC.visibility_of_element_located((By.ID, "password"))
)

# Preencher o campo de senha
password_field.send_keys("wntelecom22024")

# Enviar o formulário de login
password_field.submit()

# Aguardar redirecionamento após o login
time.sleep(20)

# Armazenar o valor do elemento em uma variável
gasto_element = WebDriverWait(driver, 5).until(
   EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.col-sm-6:nth-child(2) > div:nth-child(1) > h3:nth-child(2)'))
)

saldo_wnglobe = gasto_element.text

# Aguardar redirecionamento após o login
time.sleep(5)

# Localizar o elemento hover de relatórios
hover_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='main-menu']/li[5]/a"))
)

# Clicar no elemento hover
hover_element.click()

# Aguardar até que o elemento das ligações efetuadas esteja visível e interagível
element_ligacoes = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#main-menu > li.dropdown.menu-reports.open > ul > li:nth-child(1) > a"))
)

# Clicar no elemento das ligações efetuadas
element_ligacoes.click()

time.sleep(40)

# Armazenar o valor do elemento em uma variável
gasto_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[style="color: green"]'))
)

gastos_wnglobe = gasto_element.text

#############SALDO GERAX ######################################

# Inicializar o driver do Chrome
driver = webdriver.Chrome()

# URL de login
login_url = "https://186.194.48.100/security/login"

# Abrir a página de login
driver.get(login_url)

# Localizar o elemento hover de relatórios
hover_element = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='details-button']"))
)

# Clicar no elemento hover
hover_element.click()

# Localizar o elemento hover de relatórios
hover_element = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='proceed-link']"))
)

# Clicar no elemento hover
hover_element.click()

# Aguardar até que o campo de usuário esteja visível e interagível
username_field = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.ID, "username"))
)

# Preencher o campo de usuário
username_field.send_keys("ctxtelle")

# Aguardar até que o campo de senha esteja visível e interagível
password_field = WebDriverWait(driver, 3).until(
   EC.visibility_of_element_located((By.ID, "password"))
)

# Preencher o campo de senha
password_field.send_keys("0e3.d4d692EB")

# Enviar o formulário de login
password_field.submit()

# Aguardar redirecionamento após o login
time.sleep(20)

# Armazenar o valor do elemento em uma variável
gasto_element = WebDriverWait(driver, 5).until(
   EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.col-sm-6:nth-child(2) > div:nth-child(1) > h3:nth-child(2)'))
)
saldo_gerax6060 = gasto_element.text

# Aguardar redirecionamento após o login
time.sleep(5)

# Localizar o elemento hover de relatórios
hover_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='main-menu']/li[5]/a"))
)

# Clicar no elemento hover
hover_element.click()

# Aguardar até que o elemento das ligações efetuadas esteja visível e interagível
element_ligacoes = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#main-menu > li.dropdown.menu-reports.open > ul > li:nth-child(1) > a"))
)

# Clicar no elemento das ligações efetuadas
element_ligacoes.click()

time.sleep(40)

# Armazenar o valor do elemento em uma variável
gasto_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[style="color: green"]'))
)
gastos_gerax6060 = gasto_element.text

############# SALDO SMS ####################

# URL da API que você deseja consumir
api_url = "https://api.ctxtelle.com.br/balance"

# Cabeçalhos da requisição (se necessário)
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 523e69709c287165ab02cd518f6216e3aff2cb25"  # Exemplo de envio de token
}

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
    saldo_sms = f"Saldo: R$ {saldo}"

except requests.exceptions.RequestException as e:
    st.error(f"Erro na requisição: {e}")

# Exibir os resultados no Streamlit
st.write("#### SALDO ROTA ####")

st.write("*BFT*")
st.write("Saldo:", saldo_BFT)
st.write("Consumo até este momento: R$ ")

st.write("*TEL GLOBE*")
st.write("Saldo:  ", saldo_wnglobe)
st.write("Consumo até este momento: R$ ", gastos_wnglobe)

st.write("*SMS*")
st.write(saldo_sms)

st.write("*GERAX*")
st.write("Saldo:  ", saldo_gerax6060)
st.write("Consumo até este momento: R$ ", gastos_gerax6060)

data_hora_atual = datetime.datetime.now()
data_hora_formatada = data_hora_atual.strftime("%H:%M:%S")

st.write("*Hora da Consulta:*", data_hora_formatada)

driver.quit()
