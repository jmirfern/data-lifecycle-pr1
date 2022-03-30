import pandas as pd


def webscrap(time, name, data):
    """
    # Funció que ens arregla les taules de les diferents webs
    :param time: Hora d'extracció
    :param name: Nom de la companyia
    :param data: Dades extretes
    :return:
    """
    # Dataset amb les columnes que esperem
    columnes = ["data", "companyia", "producte", "paquet", "garantia", "cobertura"]
    # Noms de l'índex, el 0 no serveix
    garantia = data.columns.values
    # Creació del dataset
    dataset = data.rename(columns={data.columns[0]: "garantia"})
    dataset = pd.melt(dataset, id_vars="garantia", var_name="paquet", value_name="cobertura")
    dataset["producte"] = "Auto"
    dataset["companyia"] = name
    dataset["data"] = time
    return dataset[columnes]
