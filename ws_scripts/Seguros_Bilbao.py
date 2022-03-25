import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def Seguros_Bilbao():
    # Posem la URL
    URL = 'https://www.segurosbilbao.com/seguros-coche/comparativa'
    print('Llegint dades de Seguros Bilbao...')

    # Extraurem les dades HTML de la web
    orlUrl = requests.get(URL)

    # Ho pasem a text per a poder treballar
    soup = BeautifulSoup(orlUrl.text,'lxml')

    # Trobem la taula corresponent
    taula = soup.find_all("div", class_="comparison-chart-scroll")
    taula = str(taula)
    # Neteja de caracters
    taula = re.sub(r'<.*?>', lambda g: g.group(0).upper(), taula)

    # Creacio de la Data Web
    datos = pd.read_html(taula)[0]

    # Datos que necesitem
    nom = 'Seguros Bilbao'
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return datos, nom, hora
