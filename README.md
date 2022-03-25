# data-lifecycle-pr1
Projecte per la pràctica 1 de l'assignatura 
"Tipologia i Cicle de Vida de les dades"  
del màster Ciència de Dades de la Universitat Oberta de Catalunya (UOC).

Curs 2021-2022, semestre 2

## Integrants del grup

- Dario Cabrera Gurillo <dacagu@uoc.edu>
- Jonathan Mir Fernández-Aramburu <jmirfern@uoc.edu>

## Execució

Per executar l'script primer cal instal·lar les llibreries especificades
al fitxer `requirements.txt` mitjançant la següent comanda:

```
pip install -r requirements.txt
```

Després pot procedir-se a executar l'script `get_insurance_coverages.py` 
a la ruta on estigui ubicat amb la següent comanda de terminal, on `EXPORT_PATH`
és la ruta on volem desar el fitxer de destinació:

```
python get_insurance_coverages.py --export_path EXPORT_PATH
```
## Descripció dels fitxers
L'estructura del projecte és mostra a continuació:


- `/data`: Conté el dataset final
- `/docs`: Conté imatges i fitxers de suport per a la documentació
- `/ws_scripts`: Conté scripts individualitzats per a fer 
webscrapping a cada web
- `doc.md`: Document amb les respostes sol·licitades a la pràctica
- `get_insurance_coverages.py`: Fitxer principal per a executar el projecte
- `README.md`: Fitxer readme
- `requirements.txt`: Fitxer amb les llibreries a instal·lar per a la 
correcta execució del projecte

## Dataset

El dataset generat es pot descarregar des 
de [Zenodo](https://zenodo.org/record/6385595#.Yj4fiy8rxhE)

