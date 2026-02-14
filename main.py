import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM04863AA/html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraer la tabla
table = soup.find("table")
df = pd.read_html(str(table))[0]

# Guardar en CSV
df.to_csv("pbi_bcrp.csv", index=False)
