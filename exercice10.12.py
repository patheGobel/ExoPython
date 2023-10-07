""" 10.12 Utilisez les fonctions définies dans les exercices précédents pour écrire un script qui puisse 
extraire d'un texte tous les mots qui commencent par une majuscule. """
def chaineListe(chaine):
    liste = chaine
    return str(liste).split( )
def majuscule(char):
    if char in "AZERTYUIOPQSDFGHJKLMWXCVBNÀÉÈÙ":
# Demande à chatgpt s'il n'existe pas de fonction pédéfinie permettant d'avoir un seul coup 
# toutes les lettres majuscules sans avoir besoin de les lister comme ça
        return True
    else:
        return False

def traiteText(texte):
    txt=texte
    stringReceiveBecommeList=chaineListe(txt)
    listeComParMajus=[]
    for motDeLaListe in stringReceiveBecommeList:
        if (majuscule(motDeLaListe[0])):
            listeComParMajus.append(motDeLaListe)
    return listeComParMajus

text = input("Écrivez votre texte ici\n")
print(f"Voici la liste des mots commençant par des majuscules du texte que tu m'as fournis: {traiteText(text)} \n")