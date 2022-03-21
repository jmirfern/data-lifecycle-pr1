import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Posem la URL
URL = 'https://www.genesis.es/seguros-coche/comparador'

# Extraurem les dades HTML de la web
orlUrl = requests.get(URL)

# Ho pasem a text per a poder treballar
soup = BeautifulSoup(orlUrl.text,'lxml')

# Trobem la taula corresponent
taula = soup.find_all("table", class_="Tabla_Modalidades")
tabla2 = str(taula)
# Neteja de caracters
tabla2 = re.sub(r'<.*?>', lambda g: g.group(0).upper(), tabla2)

# Modificacio de valors
tabla3 = re.sub(r'::before', 'DISPONIBLE', tabla2)
df = pd.read_html(tabla3)[0]
print(df)

