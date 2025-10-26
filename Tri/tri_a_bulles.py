########################################### Exercice #################################################

def tri_bulles(tabl):
    """Trie la liste tabl par ordre croissant avec le tri à bulles"""
    n = len(...)
    for i in range(... - 1):
        for j in range(n - i - 1):
            if tabl[j] > ...: #Si la valeur suivante et plus petite alors :
                tabl[j], tabl[j + 1] = ..., ... #On échange les valeurs
    return ...

assert tri_bulles([5, 1, 4, 2, 8])  == [1, 2, 4, 5, 8]

########################################### Correction en bas #################################################



































############################################################################################

def tri_bulles(tabl):
    """Trie la liste tabl par ordre croissant avec le tri à bulles"""
    n = len(tabl)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tabl[j] > tabl[j + 1]: #Si la valeur suivante et plus petite alors :
                tabl[j], tabl[j + 1] = tabl[j + 1], tabl[j] #On échange les valeurs
    return tabl