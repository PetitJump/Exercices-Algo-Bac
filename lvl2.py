############################################################################################

def croissant(tabl):
    """Tri de manière croissante une list"""
    rendu = ... #On initialise un tableau vide
    while len(...) > ...: #Tant qu'il reste des élément non trier dans tabl on continue
        plus_petit = tabl[0]
        for k in tabl:
            if k < plus_petit:
                ... = ...
        tabl.remove(...) #On enlève à tabl la valeur la plus petite
        ... #On ajoute a rendu la valeur que l'on vient de supprimer de tabl
    return rendu

assert croissant([1, 9, 7, 54, 4, 1, 2]) == [1, 1, 2, 4, 7, 9, 54]
print("Fonction croissant() fonctionnel !")

############################################################################################