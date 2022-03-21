import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Posem la URL
URL = 'https://www.seguroscatalanaoccidente.com/seguros-coche-comparativa'


# Extraurem les dades HTML de la web
orlUrl = requests.get(URL)

# Ho pasem a text per a poder treballar
soup = BeautifulSoup(orlUrl.text,'lxml')

# Trobem la taula corresponent
taula = soup.find_all("table", class_="comparison-chart")
tabla2 = str(taula)
# Neteja de caracters
tabla2 = re.sub(r'<.*?>', lambda g: g.group(0).upper(), tabla2)
# Crearem la taula
df = pd.read_html(tabla2)[0]
print(df)
