import pandas as pd
import requests
from bs4 import BeautifulSoup
from os import path
import re

# Cambiem directori de feina
#os.path('Practica1')

# Llista on guardarem els diferents links
URL = list()

# Incorporem els links que hem guardat en el .txt
with open('/home/mp334t1/Practica1/a.txt') as urls:
    for i in urls:
    	URL.append(i)

# Eliminem els salts de linea (\n)
URL = [urls.strip() for urls in URL]
print(URL)

# Copia del http de les url
#for url in URL:
#    file_name = PurePath(url).name
#    file_path = path.join('.', file_name)
#    text = ''
#
#    try:
#        response = requests.get(url)
#        if response.ok:
#            text = response.text
#    except requests.exceptions.ConnectionError as exc:
#        print(exc)
#    
#    with open(file_path, 'w') as fh:
#        fh.write(text)
#
#    print('Written to', file_path)


# Proves
Prova = requests.get(URL[1]).content

print(Prova)
