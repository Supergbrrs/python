from flask import Flask, jsonify
import datetime
import requests
import time

app = Flask(__name__)

# Configurações da API externa
API_TOKEN = "2126e644-70bb-5739-95e9-28a97d25a2c4-3256"
API_KEY = "650a0dca-c6ab-52dc-bec3-291706619e8e-7960"

# IDs das empresas e seus respectivos limites
empresa_ids = [87, 96, 97, 98, 101, 103, 109, 110, 113, 117, 126, 127, 131, 132, 137]
limite_gastos = [460, 700, 500, 300, 3500, 200, 500, 1000, 600, 600, 300, 400, 500, 700, 500]

# Função de ícone
def get_icone(percentual):
    if percentual <= 30:
        return "🟢"
    elif percentual <= 50:
        return "🟡"
    elif percentual <= 75:
        return "🟠"
    else:
        return "🔴"

@app.route("/gastos", methods=["GET"])
def gastos_empresas():
    clientes_dados = []
    data_hoje = datetime.date.today().strftime("%Y-%m-%d")

    for idx, cliente_id in enumerate(empresa_ids):
        limite = limite_gastos[idx]

        api_url = (
            f"https://plataforma3.ctxtelle.com.br/api/profitCustomers/"
            f"{API_TOKEN}/{API_KEY}"
            f"?customers[]={cliente_id}"
            f"&date_ini={data_hoje}&date_end={data_hoje}"
            f"&time_ini=07:00:00&time_end=23:59:00"
        )

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            dados = response.json()

            if "data" in dados and dados["data"]:
                cliente = dados["data"][0]

                total_gasto = float(cliente.get('total_value', 0.00))
                percentual_utilizado = (total_gasto / limite) * 100 if limite else 0
                icone = get_icone(percentual_utilizado)

                clientes_dados.append({
                    "empresa_id": cliente_id,
                    "nome": cliente.get('customer_name', 'Desconhecido'),
                    "total_gasto": round(total_gasto, 2),
                    "limite": round(limite, 2),
                    "percentual": round(percentual_utilizado, 1),
                    "icone": icone,
                    "alerta": "⚠️ LIMITE EXCEDIDO" if percentual_utilizado > 100 else ""
                })

        except Exception as e:
            clientes_dados.append({
                "empresa_id": cliente_id,
                "erro": str(e)
            })

        time.sleep(0.2)

    return jsonify(clientes_dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

