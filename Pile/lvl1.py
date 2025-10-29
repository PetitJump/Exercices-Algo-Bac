########################### Class Pile à connaitre ##############################
class Pile:
    def __init__(self):
        """Crée une pile vide"""
        self.__data = []

    def est_vide(self):
        """Renvoie True si la pile est vide"""
        return self.__data == []

    def empiler(self, x):
        """Ajoute un élément a la pile"""
        self.__data.append(x)

    def depiler(self):
        """Retire et renvoie l'élément au sommet de la pile"""
        if self.est_vide():
            raise Exception("Pile vide")
        return self.__data.pop()

    def top(self):
        """Renvoie l'élément au sommet de la pile"""
        if self.est_vide():
            raise Exception("Pile vide")
        return self.__data[-1]

    def __repr__(self):
        """Affiche le contenu de la pile"""
        return str(self.__data)

##################################### Exercices ################################


def exo1():
    """But : finir avec p = [1, 2, 3]"""
    p = Pile()
    p.empiler(4)
    p.empiler(7)
    p.empiler(2)
    for i in range(3): #On commence par dépiler toute la Pile
        ...
    for i in range(3): #Puis on réenpile de 1 à 3
        ...
    print(p) #Il faut que lorsque on print p nous voyons [1, 2, 3]

print("Exo 1 :")
exo1()
print("Si vous voyez juste au dessus [1, 2, 3] alors tout va bien")
print("")

############################################################################################


def vider_pile(p: Pile):
    """Vide complètement la Pile p"""
    while ...: #Tant qu'il reste des éléments dans p
        print(f"On retire : {...}")

p = Pile()
p.empiler(4)
p.empiler(7)
p.empiler(2)
print("Exo vider_pile :")
vider_pile(p)
assert p.est_vide() == True
print("Fonction vider_pile fonctionnel !")

############################################################################################