"""Exercise 4: Reverse Dictionary mapping
Given:
ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
Expected Output:
{65: 'A', 66: 'B', 67: 'C', 68: 'D'}
"""
def ReverseDictionarymapping(dic):
    
    nouveau_dictionnaire = {valeur: cle for cle, valeur in dic.items()}

    return nouveau_dictionnaire
ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
print(f"{ReverseDictionarymapping(ascii_dict)}")   