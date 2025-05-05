import datetime
import requests
import json
import time
import pywhatkit as kit  # Para envio no WhatsApp

# Configurações
API_TOKEN = "2126e644-70bb-5739-95e9-28a97d25a2c4-3256"
API_KEY = "650a0dca-c6ab-52dc-bec3-291706619e8e-7960"

# IDs das empresas e seus respectivos limites
empresa_ids = [87, 96, 97, 98, 101, 103, 109, 110, 113, 117, 126, 127, 131, 132, 137]
limite_gastos = [460, 700, 500, 300, 3500, 200, 500, 1000, 600, 600, 300, 400, 500, 700, 500]

# Função para definir ícone de acordo com percentual utilizado
def get_icone(percentual):
    if percentual <= 30:
        return "🟢"
    elif percentual <= 50:
        return "🟡"
    elif percentual <= 75:
        return "🟠"
    else:
        return "🔴"

# Lista para armazenar os dados dos clientes
clientes_dados = []

# Mensagem inicial
mensagem_whatsapp = "*📊 Relatório de Gastos por Empresa (Hoje)*\n\n"

# Loop para buscar cada cliente
for idx, cliente_id in enumerate(empresa_ids):
    limite = limite_gastos[idx]

    api_url = f"https://plataforma3.ctxtelle.com.br/api/profitCustomers/{API_TOKEN}/{API_KEY}?customers[]={cliente_id}&date_ini=2025-05-02&date_end=2025-05-02&time_ini=07:00:00&time_end=23:59:00"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        dados = response.json()

        if "data" in dados and dados["data"]:
            cliente = dados["data"][0]
            clientes_dados.append(cliente)

            total_gasto = float(cliente.get('total_value', 0.00))
            percentual_utilizado = (total_gasto / limite) * 100 if limite else 0
            icone = get_icone(percentual_utilizado)

            alerta = ""
            if percentual_utilizado > 100:
                alerta = " ⚠️ *ATENÇÃO: Limite Excedido!*"

            # Monta mensagem de cada empresa
            mensagem_whatsapp += f"*{cliente.get('customer_name', 'Desconhecido')}* {icone}\n"
            mensagem_whatsapp += f"• Custo Total: *R$ {total_gasto:.2f}*\n"
            mensagem_whatsapp += f"• Limite: *R$ {limite:.2f}*\n"
            mensagem_whatsapp += f"• Utilizado: *{percentual_utilizado:.1f}%*{alerta}\n\n"

    except requests.exceptions.RequestException as e:
        mensagem_whatsapp += f"❌ Erro ao consultar Cliente {cliente_id}: {e}\n\n"

    time.sleep(0.2)  # Evitar sobrecarregar a API

# Adiciona a data/hora da consulta
data_hora_formatada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
mensagem_whatsapp += f"📅 Consulta realizada em: *{data_hora_formatada}*"

# Exibe mensagem final formatada
print("\n" + mensagem_whatsapp)

# Envio via WhatsApp
id_grupo = "Parciais%20Diários%20Cliente"  # << Coloque o número com DDI e DDD
hora_envio = datetime.datetime.now().hour
minuto_envio = datetime.datetime.now().minute + 2  # agenda para 2 minutos após agora

# Ajustar minuto/hora se ultrapassar 59
if minuto_envio >= 60:
    minuto_envio -= 60
    hora_envio += 1

# Enviar mensagem
kit.sendwhatmsg_to_group:(id_grupo, mensagem_whatsapp, hora_envio, minuto_envio)

