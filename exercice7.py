#Exercise 7: Print the following number pattern
"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5"""

def printTheFollowingNumberPattern():

    for i in range(1,6):

        for j in range(6-i):
            print(i, end=' ')
        print("\n")

printTheFollowingNumberPattern()    