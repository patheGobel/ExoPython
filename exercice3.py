#Exercise 3: Remove items from a list while iterating
def removeItemsFromListWhileIterating(liste):
    new_liste=[]
    for l in liste:
        if l<=50:
            new_liste.append(l)
    return new_liste

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"{removeItemsFromListWhileIterating(number_list)}")