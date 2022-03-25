import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def DirectSeguro():
    # Posem la URL
    URL = 'https://www.directseguros.es/seguros-de-coche/seguro-comparativa.html'

    # Extraurem les dades HTML de la web
    orlUrl = requests.get(URL)

    # Ho pasem a text per a poder treballar
    soup = BeautifulSoup(orlUrl.text,'lxml')

    # Trobem la taula corresponent
    taula = soup.find_all("div", class_="wrap-table")
    taula = str(taula)
    # Neteja de caracters
    taula = re.sub(r'<.*?>', lambda g: g.group(0).upper(), taula)

    # Modificacio de valors
    taula = re.sub(r'<IMG ALT="OPCIÓN DISPONIBLE" SRC="/WWW-IMAGENES/IMG_CHECK.PNG"/>', 'INCLUIDO', taula)
    datos = pd.read_html(taula)[0]
    datos = datos.fillna(value = 'NO INCLUIDO')

    # Reordenacio Datafram
    nom = 'Direct Seguros'
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return datos, nom, hora

