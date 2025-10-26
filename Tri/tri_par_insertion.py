########################################### Exercice #################################################

def tri_insertion(tabl):
    """Trie la liste tabl par ordre croissant avec le tri par insertion."""
    for i in range(..., len(tabl)): #On parcourt la liste à partir du deuxième élément (index 1)
        cle = tabl[i] #On prend l'élément à insérer à sa place correcte
        j = ... - 1
        while j >= 0 and ... > cle: #On décale tous les éléments plus grands que cle d'une position vers la droite
            tabl[j + 1] = ... #On déplace l'élément vers la droite
            ... -= 1 
        tabl[j + 1] = ... #On place la cle à sa position correcte
    return ...

assert tri_insertion([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5]

########################################### Correction en bas #################################################

































def tri_insertion(tabl):
    """Trie la liste tabl par ordre croissant avec le tri par insertion."""
    for i in range(1, len(tabl)): #On parcourt la liste à partir du deuxième élément (index 1)
        cle = tabl[i] #On prend l'élément à insérer à sa place correcte
        j = i - 1
        while j >= 0 and tabl[j] > cle: #On décale tous les éléments plus grands que cle d'une position vers la droite
            tabl[j + 1] = tabl[j] #On déplace l'élément vers la droite
            j -= 1
        tabl[j + 1] = cle #On place la cle à sa position correcte
    return tabl