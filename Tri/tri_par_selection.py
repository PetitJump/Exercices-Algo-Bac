########################################### Exercice #################################################

def tri_selection(tabl):
    """Trie la liste tabl par ordre croissant avec le tri par sélection."""
    n = len(...)
    for i in range(... - 1):
        min_i = ... #Index du plus petit nombre dans tabl
        for j in range(i + 1, ...): #En suivant la métode range(start, stop, step)
            if tabl[j] < ...: #Si la valeur que l'on regarde est plus petite que celle qu'on avait défini alors:
                min_i = ...
        tabl[i], tabl[min_i] = ..., ... #On échange les valeurs
    return ...

assert (tri_selection([4, 2, 5, 1, 3])) == [1, 2, 3, 4, 5]

########################################### Correction en bas #################################################

































def tri_selection(tabl):
    """Trie la liste tabl par ordre croissant avec le tri par sélection."""
    n = len(tabl)
    for i in range(n - 1):
        min_i = i #Index du plus petit nombre dans tabl
        for j in range(i + 1, n): #En suivant la métode range(start, stop, step)
            if tabl[j] < tabl[min_i]: #Si la valeur que l'on regarde est plus petite que celle qu'on avait défini alors:
                min_i = j
        tabl[i], tabl[min_i] = tabl[min_i], tabl[i] #On échange les valeurs
    return tabl 