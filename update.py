name: Atualizar Abastecimento

on:
  repository_dispatch:
    types: [atualizar]

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Atualizar index.html com dados do Forms
        run: |
          NOME="${{ github.event.client_payload.nome }}"
          LANCHES="${{ github.event.client_payload.lanches }}"
          OBSERVACAO="${{ github.event.client_payload.observacao }}"
          
          cat > index.html << EOF
          <!DOCTYPE html>
          <html lang="pt-br">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Abastecimento do Dia</title>
            <style>
              body { font-family: Arial, sans-serif; background-color: #f4f4f4; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
              .card { background: white; border-radius: 15px; padding: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); max-width: 400px; width: 90%; text-align: center; }
              h1 { color: #6B2D8B; font-size: 24px; }
              .info { margin: 15px 0; }
              .label { color: #888; font-size: 14px; }
              .valor { font-weight: bold; color: #333; font-size: 20px; }
            </style>
          </head>
          <body>
            <div class="card">
              <h1>🥪 Abastecimento do Dia</h1>
              <div class="info">
                <div class="label">Quem Abasteceu</div>
                <div class="valor">$NOME</div>
              </div>
              <div class="info">
                <div class="label">Lanches</div>
                <div class="valor">$LANCHES</div>
              </div>
              <div class="info">
                <div class="label">Observação</div>
                <div class="valor">$OBSERVACAO</div>
              </div>
              <div class="info">
                <div class="label">Horário</div>
                <div class="valor">$(date '+%d/%m/%Y %H:%M')</div>
              </div>
            </div>
          </body>
          </html>
          EOF

      - name: Commit e Push
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "GitHub Action"
          git add index.html
          git commit -m "Atualizar abastecimento do dia" || echo "Sem mudanças"
          git push
