import os
import re

nome = os.environ.get("NOME", "")
lanches_raw = os.environ.get("LANCHES", "")
observacao = os.environ.get("OBSERVACAO", "").strip()

# Limpa os lanches removendo colchetes e aspas
lanches_list = re.findall(r'"([^"]+)"', lanches_raw)
if not lanches_list:
    lanches_list = [lanches_raw.strip("[]\" ")]
lanches_html = "<br>".join(f"🥪 {l}" for l in lanches_list if l)

# Observação só aparece se preenchida
obs_html = f"""
    <div class="info">
      <div class="label">Observação</div>
      <div class="valor">{observacao}</div>
    </div>""" if observacao else ""

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
    .valor {{ font-weight: bold; color: #333; font-size: 20px; line-height: 1.6; }}
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
      <div class="valor">{lanches_html}</div>
    </div>
    {obs_html}
    <div class="info">
      <div class="label">Horário</div>
      <div class="valor">HORARIO_PLACEHOLDER</div>
    </div>
  </div>
</body>
</html>"""

from datetime import datetime
horario = datetime.now().strftime("%d/%m/%Y %H:%M")
html = html.replace("HORARIO_PLACEHOLDER", horario)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html atualizado!")
