import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def Mutua():
    # Posem la URL
    URL = 'https://www.mutua.es/seguros-coche/comparador/'

    # Extraurem les dades HTML de la web
    orlUrl = requests.get(URL)

    # Ho pasem a text per a poder treballar
    soup = BeautifulSoup(orlUrl.text,'lxml')

    # Trobem la taula corresponent
    taula = soup.find_all("table", class_="productTable break-titleCell-on-phones moreTopMargin")
    taula = str(taula)
    # Neteja de caracters
    taula = re.sub(r'<.*?>', lambda g: g.group(0).upper(), taula)

    # Modificacio de valors
    taula = re.sub(r'<IMG ALT="INCLUIDO" SRC="/DIGITAL/RECURSOS/IMG/ICOTABOK.PNG" TITLE="INCLUIDO"/>', 'INCLUIDO', taula)
    taula = re.sub(r'<IMG ALT="NO INCLUIDO" SRC="/DIGITAL/RECURSOS/IMG/ICOTABKO.PNG" TITLE="NO INCLUIDO"/>', 'NO INCLUIDO', taula)
    df = pd.read_html(taula)[0]

    # Arreglem la taula, llevem les files dobles del HTML
    lista = [i for i in range(0,len(df)) if i%2==1]
    datos = pd.DataFrame(df.iloc[lista]).reset_index()
    # Dades a analitzar
    nom = 'Mutua Madrileña'
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return datos, nom, hora
