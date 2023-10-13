"""Exercise 6: Filter dictionary to contain keys present in the given list
Given:

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']
Expected Output: -

new dict {'A': 65, 'C': 67, 'F': 70}"""

def filterDictionaryToContainKeysPresentInTheGivenList(D1, L1):
    newDic={}
    for cle, val in D1.items():
        if cle in L1:
            newDic.setdefault(cle, val)
    return newDic

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']
print(f"new dict {filterDictionaryToContainKeysPresentInTheGivenList(d1, l1)}")