############################################################################################

def plus_gand(tabl: list[int]) -> int:
    """Renvoie la valeur la plus grande d'un tableau"""
    actuel = ... #On initialise la plus grande valeur avec le premier chiffre du tableau
    for k in tabl:
        if k > ...:
            actuel = ... #On met le nouveau plus grand nombre dans actuel
    return ...

assert plus_gand([1, 2, 7, 3, 4, 5]) == 7 #La fonction plusgrand() doit renvoyer 7 car c'est la valeur la plus grande dans [1, 2, 7, 3, 4, 5]
print("Fonction plus_grand() fonctionnel !")

############################################################################################

def inverser(tabl: list) -> list:
    """Inverse une liste"""
    rendu = []
    for i in range(len(tabl), ..., -1): #On commence a i=len(tabl) puis i-=1 à chaque boucle ; on s'arretera ensuite lorsque i=0. On utilise ici le range(start, stop, step)
        rendu.append(tabl[...]) #On ajoute à rendu la valeur que l'on traite actuelement
    return ...

assert inverser([1, 2, 3]) == [3, 2, 1] 
print("Fonction inverser() fonctionnel !")

############################################################################################

def rechercher(tabl: list, x) -> int:
    """Recherche x dans le tableau et renvoie la valeur où il y était dans le tableu"""
    for i in range(...):
        if ... == x:
            return ...

assert rechercher([1, 2, 34, "a", "S.Meden", 324, 4], 4) == 6
assert rechercher([1, 2, 34, "a", "S.Meden", 324, 4], "a") == 3
print("Fonction rechercher() fonctionnel !")

############################################################################################