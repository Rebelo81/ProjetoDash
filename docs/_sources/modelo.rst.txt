Modelo de Machine Learning
==========================

Esta seção apresenta os detalhes do modelo de aprendizado de máquina utilizado no ProjetoDash, incluindo o processo de treinamento, persistência e aplicação prática via interface interativa desenvolvida com Dash.

Treinamento do Modelo
---------------------

O modelo foi treinado com a biblioteca `XGBoost`, amplamente utilizada para tarefas de classificação e regressão devido à sua alta performance e capacidade de lidar com dados tabulares complexos.

As etapas de pré-processamento incluíram:

- Análise exploratória dos dados
- Normalização e tratamento de valores nulos
- Divisão entre dados de treino e teste
- Avaliação com métricas como **acurácia**, **precisão** e **matriz de confusão**

O script responsável pelo treinamento foi o:


Este script lê os dados, treina o modelo XGBoost e o salva para uso posterior com o `joblib`.

Persistência do Modelo
----------------------

Após o treinamento, o modelo foi salvo no formato `.pkl` usando a biblioteca `joblib`, permitindo reutilização futura sem necessidade de reentreinamento.  

Arquivos gerados:

- `modelo_xgboost.pkl` → modelo treinado
- `medianas.pkl` → valores médios usados no preenchimento de dados ausentes no formulário de predição

Aplicação no Dashboard
----------------------

O modelo foi integrado ao aplicativo Dash, permitindo previsões em tempo real diretamente pela interface web. O módulo `formulario.py` é responsável por:

- Captar os dados inseridos pelo usuário
- Aplicar transformações idênticas ao pipeline de treinamento
- Carregar o modelo persistido
- Realizar a predição e exibir o resultado visualmente

Testes Automatizados
--------------------

Toda a aplicação está integrada com testes automatizados desenvolvidos com `Selenium` e `Pytest`, garantindo que:

- A interface web esteja acessível
- As páginas essenciais estejam funcionando (inicial, formulário e gráficos)
- O modelo responda conforme esperado a entradas válidas

Além disso, a geração de prints automatizados e relatórios HTML permite fácil validação dos testes por qualquer membro da equipe.

Pipeline de Integração Contínua
-------------------------------

Utilizamos `Jenkins` para orquestrar o processo de integração contínua (CI). O pipeline realiza:

1. Clone do repositório
2. Instalação de dependências
3. Execução de testes automatizados (`pytest`)
4. Análise estática do código com `flake8`

Este processo garante qualidade de código, testes e entregas confiáveis em produção.

