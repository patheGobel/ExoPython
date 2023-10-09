def replaceNewLinesWithSpace():
    with open("/home/pathegobelba/Documents/MyCodes/Python/exo/sample.txt", "w+") as file:
        text=input("Écrivez votre texte dans le fichier\n")
#Écriture dans le fichier
        file.write(text)
#Revenir au début du fichier
        file.seek(0)
#Lire le contenu du fichier
        contenu=file.read()
        print("Contenu du fichier :", contenu)
#mettre le contenu fichier sur une liste dont les élément seront
#les différentes lignes
    tableauDesLignes = []
    for lignes in contenu:
        if lignes == '\n':
            tableauDesLignes.append(lignes)
    print(tableauDesLignes)            
        
replaceNewLinesWithSpace()    