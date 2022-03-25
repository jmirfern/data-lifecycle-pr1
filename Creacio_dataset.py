import pandas as pd
from Scripts_Webs.Catalana_Occidente import Catalanaoccidnete
from Scripts_Webs.DirectSeguro import DirectSeguro
from Scripts_Webs.MMTSEGUROS import MMTSEGUROS
from Scripts_Webs.Mutua import Mutua
from Scripts_Webs.RACC import RACC
from Scripts_Webs.Seguros_Bilbao import Seguros_Bilbao
# Funcio que ens arregla les taules de les diferents webs
def Creacio_Dataset(Hora, Nom, Datos):
    # Dataset amb les columnes que esperem
    dataset = pd.DataFrame(columns = ['data','companyia','producte','paquet','garantia','cobertura'])
    # Noms del index, el 0 no serveix
    garantia = Datos.columns.values
    # Creacio del dataset
    for i in range(1,len(garantia)):
        for j in range(len(Datos)):
             dataset = dataset.append({
                    'data': Hora, 
                    'companyia' : Nom,
                    'producte':'Auto',
                    'paquet': str(Datos[garantia[0]][j]), 
                    'garantia': str(garantia[i]),
                    'cobertura' : Datos[garantia[i]][j]}, ignore_index=True)

    return dataset

# Extraccio de Dades dels diferents Scripts Webs
Datos1, nom1, hora1 = Catalanaoccidnete()
Datos2, nom2, hora2 = DirectSeguro()
Datos3, nom3, hora3 = MMTSEGUROS()
Datos4, nom4, hora4 = Mutua()
Datos5, nom5, hora5 = RACC()
Datos6, nom6, hora6 = Seguros_Bilbao()

# Preparem les dades
Datos = [Datos1, Datos2, Datos3, Datos4, Datos5, Datos6]
Nom = [nom1, nom2, nom3, nom4, nom5, nom6]
Hora = [hora1, hora2, hora3, hora4, hora5, hora6]

# Dataframe buit
df = pd.DataFrame()

for i in range(0, len(Datos)):
    df = df.append(Creacio_Dataset(Hora[i], Nom[i], Datos[i]), ignore_index=True)

df.to_csv('Comparacio_cobertures_auto.csv')
