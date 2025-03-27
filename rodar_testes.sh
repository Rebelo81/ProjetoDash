#!/bin/bash

echo "🔁 Ativando ambiente virtual..."
source venv/Scripts/activate

echo "🚀 Executando testes com Pytest..."
pytest tests/ --html=relatorio_home.html --self-contained-html

echo "✅ Testes finalizados. Relatório gerado em: relatorio_home.html"

# Abrir o relatório automaticamente no navegador (Windows)
explorer.exe relatorio_home.html
