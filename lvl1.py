
def plus_gand(tabl: list[int]) -> int:
    """Renvoie la valeur la plus grande d'un tableau"""
    actuel = ... #On initialise la plus grande valeur avec le premier chiffre du tableau
    for k in tabl:
        if k > ...:
            actuel = ... #On met le nouveau plus grand nombre dans actuel
    return ...

assert plus_gand([1, 2, 7, 3, 4, 5]) == 7 #La fonction plusgrand() doit renvoyer 7 car c'est la valeur la plus grande dans [1, 2, 7, 3, 4, 5]
print("Fonction plus_grand() fonctionnel !")


def inverser(tabl: list):
    """Inverse une liste"""