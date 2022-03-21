import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Posem la URL
URL = 'https://www.mutua.es/seguros-coche/comparador/'

# Extraurem les dades HTML de la web
orlUrl = requests.get(URL)

# Ho pasem a text per a poder treballar
soup = BeautifulSoup(orlUrl.text,'lxml')

# Trobem la taula corresponent
taula = soup.find_all("table", class_="productTable break-titleCell-on-phones moreTopMargin")
tabla2 = str(taula)
# Neteja de caracters
tabla2 = re.sub(r'<.*?>', lambda g: g.group(0).upper(), tabla2)

# Modificacio de valors
tabla2 = re.sub(r'<IMG ALT="INCLUIDO" SRC="/DIGITAL/RECURSOS/IMG/ICOTABOK.PNG" TITLE="INCLUIDO"/>', 'INCLUIDO', tabla2)
tabla2 = re.sub(r'<IMG ALT="NO INCLUIDO" SRC="/DIGITAL/RECURSOS/IMG/ICOTABKO.PNG" TITLE="NO INCLUIDO"/>', 'NO INCLUIDO', tabla2)
df = pd.read_html(tabla2)[0]
print(df)

