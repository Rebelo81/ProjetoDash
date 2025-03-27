from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Caminho correto para o ChromeDriver no seu projeto
caminho_driver = "chrome-test/chromedriver-win64/chromedriver.exe"

# Caminho para o Chrome for Testing (navegador alternativo, se quiser usar)
# chrome_path = "chrome-test/chrome-win64/chrome.exe"  # descomente se necessário

# Configurações do Chrome
chrome_options = webdriver.ChromeOptions()

# Se quiser usar o Chrome for Testing baixado manualmente, descomente abaixo:
# chrome_options.binary_location = chrome_path

# Inicializa o driver com o caminho do executável
service = Service(executable_path=caminho_driver)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL da sua aplicação Dash local
url = "http://127.0.0.1:8080"

# Teste da página inicial
driver.get(url)
time.sleep(10)
assert "Dash" in driver.title
assert "pagina inicial" in driver.page_source
print("✅ Teste da página inicial com sucesso!")

# Teste da página do formulário
driver.get(url + "/formulario")
time.sleep(10)
assert "Dashboard - Formulario" in driver.title
assert "Formulario" in driver.page_source
print("✅ Teste da página do formulário com sucesso!")

# Teste da página de gráficos
driver.get(url + "/graficos")
time.sleep(10)
assert "Dashboard - Graficos" in driver.title
assert "Graficos" in driver.page_source
print("✅ Teste da página de gráficos com sucesso!")

# Encerra o navegador
driver.quit()

