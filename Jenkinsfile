pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "🔄 Clonando o repositório..."
                git 'https://github.com/Rebelo81/ProjetoDash.git'
            }
        }

        stage('Análise Estática') {
            steps {
                echo "🔍 Rodando análise estática com Flake8..."
                sh 'flake8 --ignore=W291,W293,W391 ./*.py || true'
            }
        }

        stage('Testes Automatizados') {
            steps {
                echo "🧪 Executando testes com Pytest..."
                sh 'pytest --html=relatorio_home.html --self-contained-html || true_
