#Exercise 3: Remove items from a list while iterating
def removeItemsFromListWhileIterating(liste):
    
    return [n for n in liste if n<=50]

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"{removeItemsFromListWhileIterating(number_list)}")   