import csv

open('celulas.yaml', 'w').close()
open('trenes.yaml', 'w').close()
fcel = open("celulas.yaml", "wt")
ftren = open("trenes.yaml", "wt")
lista = []

with open('cel-tren.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        # Crear trenes
        if not row["tren"] in lista:
            ftren.write("apiVersion: backstage.io/v1alpha1\n")
            ftren.write("kind: Group\n")
            ftren.write("metadata:\n")
            ftren.write("   name: " + row["tren"].replace(" ", "-").lower() + "\n")
            ftren.write("   description: " + row["tren"] + "\n")
            ftren.write("spec:\n")
            ftren.write("   type: team\n")
            ftren.write("   children: []\n")
            ftren.write("---\n")
            lista.append(row["tren"])
        # Crear celulas
        if not (row["celula"] == ""):
            fcel.write("apiVersion: backstage.io/v1alpha1\n")
            fcel.write("kind: Group\n")
            fcel.write("metadata:\n")
            fcel.write("   name: " + row["celula"].replace(" ", "-").lower() + "\n")
            fcel.write("   description: " + row["celula"] + "\n")
            fcel.write("spec:\n")
            fcel.write("   type: team\n")
            fcel.write("   parent: " + row["tren"].replace(" ", "-").lower()+ "\n" )
            fcel.write("   children: []\n")
            fcel.write("---\n")
    fcel.close()
    ftren.close()


 
