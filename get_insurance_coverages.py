import os
import argparse
import pandas as pd
from ws_scripts.Catalana_Occidente import Catalanaoccidnete
from ws_scripts.DirectSeguro import DirectSeguro
from ws_scripts.MMTSEGUROS import MMTSEGUROS
from ws_scripts.RACC import RACC
from ws_scripts.Seguros_Bilbao import Seguros_Bilbao
from ws_scripts import create_dataset


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--export_path", help="Entra la ruta per exportar el fitxer de sortida csv")
    args = parser.parse_args()
    webscrap_insurance_webs(output_path=args.export_path)


def webscrap_insurance_webs(output_path):
    # Extracció de Dades dels diferents Scripts Webs
    dades1, nom1, hora1 = Catalanaoccidnete()
    dades2, nom2, hora2 = DirectSeguro()
    dades3, nom3, hora3 = MMTSEGUROS()
    dades4, nom4, hora4 = RACC()
    dades5, nom5, hora5 = Seguros_Bilbao()

    # Preparem les dades
    dades = [dades1, dades2, dades3, dades4, dades5]
    nom = [nom1, nom2, nom3, nom4, nom5]
    hora = [hora1, hora2, hora3, hora4, hora5]

    # Dataframe buit
    df_list = []

    for k in range(0, len(dades)):
        df_list.append(create_dataset.webscrap(time=hora[k], name=nom[k], data=dades[k]))


    df = pd.concat(df_list)
    ruta = os.path.join(output_path, 'data/comparacio_cobertures_auto.csv')
    print("Fitxer csv exportat a: ")
    print(str(ruta))
    df.to_csv(ruta)


if __name__ == '__main__':
    main()
