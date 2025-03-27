import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Caminhos específicos do seu projeto:
CHROMEDRIVER_PATH = "chrome-test/chromedriver-win64/chromedriver.exe"
CHROME_BINARY_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"

@pytest.fixture(scope="module")
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')         # Executa sem abrir o navegador
    chrome_options.add_argument('--disable-gpu')      # Desativa aceleração gráfica
    chrome_options.add_argument('--window-size=1920,1080')  # Tamanho da janela
    chrome_options.binary_location = CHROME_BINARY_PATH

    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()

