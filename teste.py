import os

def ouvrir_fichier(fichier):
    try:
        # Utilisez la commande "open" du système d'exploitation pour ouvrir le fichier
        os.system(f"open {fichier}")  # Sur macOS
        #os.system(f'start {fichier}') # Sur Windows

        print(f"Fichier {fichier} ouvert avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier : {e}")

# Utilisation de la fonction pour ouvrir un fichier
fichier_a_ouvrir = "/home/pathegobelba/Documents/MyCodes/Python/exo/sample.txt"
ouvrir_fichier(fichier_a_ouvrir)
  