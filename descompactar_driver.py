import zipfile

with zipfile.ZipFile("chromedriver-win64.zip", 'r') as zip_ref:
    zip_ref.extractall("chrome-test")
    
print("✅ ChromeDriver extraído com sucesso!")
