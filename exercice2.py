import os
def replaceNewLinesWithSpace():

    def ouvrir_fichier(fichier):
        try:
            # Utilisez la commande "open" du système d'exploitation pour ouvrir le fichier
            os.system(f"open {fichier}")  # Sur macOS

            print(f"Fichier {fichier} ouvert avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'ouverture du fichier : {e}")

    # Utilisation de la fonction pour ouvrir un fichier
    fichier_a_ouvrir = "/home/pathegobelba/Documents/MyCodes/Python/exo/sample.txt"
    ouvrir_fichier(fichier_a_ouvrir)
#Lire le contenu du fichier
    with open("/home/pathegobelba/Documents/MyCodes/Python/exo/sample.txt", "r") as file:
        contenu=file.read()
#Contenu avant modification
        print("Contenu du fichier :", contenu)
        lignes = contenu.replace('\n', ' ')
#contenu après modification        
        print("Contenu du fichier avant la modification :", contenu)
replaceNewLinesWithSpace()    