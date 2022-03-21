import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Posem la URL
URL = 'https://www.directseguros.es/seguros-de-coche/seguro-comparativa.html'

# Extraurem les dades HTML de la web
orlUrl = requests.get(URL)

# Ho pasem a text per a poder treballar
soup = BeautifulSoup(orlUrl.text,'lxml')

# Trobem la taula corresponent
taula = soup.find_all("div", class_="wrap-table")
tabla2 = str(taula)
# Neteja de caracters
tabla2 = re.sub(r'<.*?>', lambda g: g.group(0).upper(), tabla2)

# Modificacio de valors
tabla3 = re.sub(r'<IMG ALT="OPCIÓN DISPONIBLE" SRC="/WWW-IMAGENES/IMG_CHECK.PNG"/>', 'DISPONIBLE', tabla2)
df = pd.read_html(tabla3)[0]
df = df.fillna(value = 'NO DISPONIBLE')
print(df)

