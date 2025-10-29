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