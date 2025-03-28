# 📊 Projeto Dash com Machine Learning e Jenkins

Este projeto é uma aplicação web interativa desenvolvida com Dash e Python. Ele integra:

- Análise de dados com gráficos dinâmicos
- Formulário interativo
- Modelo de Machine Learning para previsão
- Testes automatizados com Pytest e Selenium
- Análise de qualidade com Flake8
- Geração de documentação com Sphinx
- Pipeline CI/CD com Jenkins
- Docker para empacotamento da aplicação

---

## 🚀 Tecnologias utilizadas

- Python 3.10
- Dash & Plotly
- Dash Bootstrap Components
- Pandas & Numpy
- XGBoost
- Pytest
- Flake8
- Sphinx
- Docker
- Jenkins

---

## 🧠 Modelo de Machine Learning

O modelo foi treinado com XGBoost para prever padrões com base em dados históricos. A pipeline inclui:

- Pré-processamento de dados
- Treinamento do modelo
- Persistência do modelo (`.pkl`)
- Previsões feitas em tempo real na interface web

---

## 🧪 Testes Automatizados

- Framework: Pytest
- Testes funcionais com Selenium
- Prints de evidências salvos na pasta `testes_evidencias/`
- Geração de relatório em HTML (`relatorio_home.html`)

---

## 📘 Documentação

A documentação é gerada com Sphinx e está localizada na pasta `source/`. Inclui:

- Modelo de ML
- Etapas do pipeline
- Manual de uso

Para gerar manualmente:

```bash
sphinx-build -b html source/ build/html

