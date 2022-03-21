import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Posem la URL
URL = 'https://www.racc.es/seguro-coche/'

# Extraurem les dades HTML de la web
orlUrl = requests.get(URL)

# Ho pasem a text per a poder treballar
soup = BeautifulSoup(orlUrl.text,'lxml')

# Trobem la taula corresponent
taula = soup.find_all("table", class_="date-table2")
tabla2 = str(taula)
# Neteja de caracters
tabla2 = re.sub(r'<.*?>', lambda g: g.group(0).upper(), tabla2)

# Modificacio de valors
tabla2 = re.sub(r'<IMG ALT="" CLASS="LAZYLOAD ALIGNCENTER" DATA-ORIG-SRC="HTTPS://WWW.RACC.ES/WP-CONTENT/UPLOADS/2021/01/BLOBSERVER.PNG" SRC="DATA:IMAGE/GIF;BASE64,R0LGODLHAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOW==" WIDTH=""/>', 'INCLUIDO', tabla2)
tabla2 = re.sub(r'<IMG ALT="" CLASS="LAZYLOAD" DATA-ORIG-SRC="HTTPS://WWW.RACC.ES/WP-CONTENT/UPLOADS/2021/01/BLOBSERVER.PNG" SRC="DATA:IMAGE/GIF;BASE64,R0LGODLHAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOW==" WIDTH=""/>', 'INCLUIDO', tabla2)
df = pd.read_html(tabla2)[0]
df = df.fillna(value = 'NO INCLUIDO')
print(df)

