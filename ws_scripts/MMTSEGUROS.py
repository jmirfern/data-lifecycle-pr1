import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def MMTSEGUROS():
    # Posem la URL
    URL = 'https://www.mmtseguros.com/seguros-coche/comparador-seguros-coche/'
    print('Llegint dades de MMT SEGUROS...')
    # Extraurem les dades HTML de la web
    orlUrl = requests.get(URL)

    # Ho pasem a text per a poder treballar
    soup = BeautifulSoup(orlUrl.text,'lxml')

    # Trobem la taula corresponent
    taula = soup.find_all("div", class_="tcomparador")
    taula = str(taula)
    # Neteja de caracters
    taula = re.sub(r'<.*?>', lambda g: g.group(0).upper(), taula)

    #Modificacions
    taula = re.sub(r'<SPAN CLASS="OK"></SPAN>', 'INCLUIDO', taula)
    taula = re.sub(r'<SPAN CLASS="OKS"></SPAN>', 'INCLUIDO (SEGUN FRANQUICIA)', taula)


    # Modificacio de valors
    datos = pd.read_html(taula)[0]

    # Arreglem la taula
    datos = datos.drop(16)
    Signo = datos['Terceros'][7]
    datos = datos.replace( Signo, 'NO INCLUIDO')

    # Dades a obtindre
    nom = 'MMT Seguros'
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return datos, nom, hora

