import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def RACC():
    # Posem la URL
    URL = 'https://www.racc.es/seguro-coche/'

    # Extraurem les dades HTML de la web
    orlUrl = requests.get(URL)

    # Ho pasem a text per a poder treballar
    soup = BeautifulSoup(orlUrl.text,'lxml')

    # Trobem la taula corresponent
    taula = soup.find_all("table", class_="date-table2")
    taula = str(taula)
    # Neteja de caracters
    taula = re.sub(r'<.*?>', lambda g: g.group(0).upper(), taula)

    # Modificacio de valors
    taula = re.sub(r'<IMG ALT="" CLASS="LAZYLOAD ALIGNCENTER" DATA-ORIG-SRC="HTTPS://WWW.RACC.ES/WP-CONTENT/UPLOADS/2021/01/BLOBSERVER.PNG" SRC="DATA:IMAGE/GIF;BASE64,R0LGODLHAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOW==" WIDTH=""/>', 'INCLUIDO', taula)
    taula = re.sub(r'<IMG ALT="" CLASS="LAZYLOAD" DATA-ORIG-SRC="HTTPS://WWW.RACC.ES/WP-CONTENT/UPLOADS/2021/01/BLOBSERVER.PNG" SRC="DATA:IMAGE/GIF;BASE64,R0LGODLHAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOW==" WIDTH=""/>', 'INCLUIDO', taula)
    datos = pd.read_html(taula)[0]
    datos = datos.fillna(value = 'NO INCLUIDO')
    Signo = datos['TERCEROS'][5]
    datos = datos.replace( Signo, 'NO INCLUIDO')


    # Datos que necesitem
    nom = 'RACC'
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return datos, nom, hora