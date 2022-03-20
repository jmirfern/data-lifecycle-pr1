import pandas as pd
import requests
from bs4 import BeautifulSoup
from os import path
import re

# Cambiem directori de feina
#os.path('Practica1')
# Aquest codi funciona per a les asseguradores:
# Catalana Occidente,

# Llista on guardarem els diferents links
URL = list()

# Incorporem els links que hem guardat en el .txt
with open('/home/mp334t1/Practica1/a.txt') as urls:
    for i in urls:
    	URL.append(i)

# Eliminem els salts de linea (\n)
URL = [urls.strip() for urls in URL]


# Extraurem les dades HTML de la web, farem el cas particular del 2
orlUrl = requests.get(URL[2])

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
