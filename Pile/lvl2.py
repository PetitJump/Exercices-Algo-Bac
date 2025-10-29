from lvl1 import Pile

############################################################################################

def inverser_liste(liste: list) -> list:
    """Inverse une list avec l'utilisation de Pile"""
    p = Pile()
    for k in liste: #On met tout les élément de listes dans p
        ... 
    
    res = []
    while ...: #Tant qu'il reste des éléments dans p
        ... #On ajoute a res les éléments de p (avec la méthode LIFO)
    return res

assert inverser_liste([1, 2, 3]) == [3, 2, 1]

############################################################################################
#Classique du Bac

def verif_parentheses(chaine: str) -> bool:
    """Verifie si une structure avec des parenthèse est bien construite"""
    p = Pile()
    for k in chaine:
        if ...: #Si k est une parenthese ouvrante
            p.empiler(...)
        elif ...: #Si k est une parenthese fermante
            if ...: #Si p est vide
                return False
            ... #On dépile
    return p.est_vide()

assert verif_parentheses("() ()") == True
assert verif_parentheses("((())) ())") == False
############################################################################################