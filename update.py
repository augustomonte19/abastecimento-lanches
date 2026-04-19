import json
import urllib.request

# Lê o dados.json do SharePoint
url = "https://capriccheadm.sharepoint.com/sites/AbastecimentoLanches/Documentos%20Compartilhados/dados.json"

try:
    with urllib.request.urlopen(url) as response:
        dados = json.loads(response.read().decode())
        ultimo = dados[-1] if dados else {}
except:
    ultimo = {}

# Pega os valores
nome = ultimo.get("Quem_Abasteceu", "Aguardando...")
lanches = ultimo.get("Lanches", "Aguardando...")
obs = ultimo.get("Obs", "Aguardando...")
horario = ultimo.get("Data_Hora_Envio", "Aguardando...")

# Atualiza o index.html
html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abastecimento do Dia</title>
  <style>
    body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }}
    .card {{ background: white; border-radius: 15px; padding: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); max-width: 400px; width: 90%; text-align: center; }}
    h1 {{ color: #6B2D8B; font-size: 24px; }}
    .info {{ margin: 15px 0; }}
    .label {{ color: #888; font-size: 14px; }}
    .valor {{ font-weight: bold; color: #333; font-size: 20px; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>🥪 Abastecimento do Dia</h1>
    <div class="info">
      <div class="label">Quem Abasteceu</div>
      <div class="valor">{nome}</div>
    </div>
    <div class="info">
      <div class="label">Lanches</div>
      <div class="valor">{lanches}</div>
    </div>
    <div class="info">
      <div class="label">Observação</div>
      <div class="valor">{obs}</div>
    </div>
    <div class="info">
      <div class="label">Horário</div>
      <div class="valor">{horario}</div>
    </div>
  </div>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html atualizado com sucesso!")
