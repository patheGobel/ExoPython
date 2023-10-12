#Exercise 5: Display all duplicate items from a list
"""Exercise 4: Reverse Dictionary mapping
Given:
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
Expected Output:
[20, 60, 30]
"""
def displayAllDuplicateItemsFromList(liste):
    
    elements_vus = set()
    doublons = set()


    for element in liste:
        if element in elements_vus:
            doublons.add(element)
        else:
            elements_vus.add(element)

    return list(doublons) 
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
print(f"{displayAllDuplicateItemsFromList(sample_list)}")