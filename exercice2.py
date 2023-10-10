def replaceNewLinesWithSpace():
#Ouvrir un fichier 
    with open("/home/pathegobelba/Documents/MyCodes/Python/exo/sample.txt", "w") as file:
        file.write("ligne1\nligne2\nligne3\nligne4\nligne5\n")
#Lire le contenu du fichier
    with open("/home/pathegobelba/Documents/MyCodes/Python/exo/sample.txt", "r") as file:
        contenu=file.read()
#Contenu avant modification
        print("Contenu du fichier :", contenu)
        lignes = contenu.replace('\n', ' ')
#contenu après modification        
        print("Contenu du fichier avant la modification :", lignes)
replaceNewLinesWithSpace()    