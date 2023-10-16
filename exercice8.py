"""Exercise 8: Create an inner function
Question description: -

Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
Create an inner function inside an outer function that will concatenate x and y.
At last, an outer function will join the word 'developer' to it.
Expected Output: -

EmmaKellyDevelopers"""

def outerFunction(xx, yy):
    a = xx
    b = yy
    def innerFunctionConcatenater(a, b):
        return a + b


    # Appeler la fonction interne et retourner la valeur
    return innerFunctionConcatenater(a, b)


def outerJoinner():
    x = "Emma"
    y = "Kelly"
    return outerFunction(x, y)+"Developers"




resultat = outerJoinner()
print(f"{resultat}")