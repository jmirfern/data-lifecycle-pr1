import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


def Catalanaoccidnete():
    # Posem la URL
    URL = 'https://www.seguroscatalanaoccidente.com/seguros-coche-comparativa'
    print('Llegint dades de Catalana Occidente...')

    # Extraurem les dades HTML de la web
    orlUrl = requests.get(URL)

    # Ho pasem a text per a poder treballar
    soup = BeautifulSoup(orlUrl.text,'lxml')

    # Trobem la taula corresponent
    taula = soup.find_all("table", class_="comparison-chart")
    taula = str(taula)
    # Neteja de caracters
    taula = re.sub(r'<.*?>', lambda g: g.group(0).upper(), taula)
    # Crearem la taula que hem extret
    Datos = pd.read_html(taula)[0]

    # Registre
    nom = 'Catalana Occidente'
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return Datos, nom, hora
