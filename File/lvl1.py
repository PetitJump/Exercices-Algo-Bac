########################### Class File à connaitre ##############################
class File:
    def __init__(self, t):
        self.__taille = t
        self.__data = [None] * self.__taille
        self.__start = 0
        self.__end = 0

    def est_vide(self):
        return self.__start == self.__end
    
    def est_pleine(self):
        return self.__end - self.__start == self.__taille 

    def enfiler(self, x):
        if self.est_pleine():
            raise Exception('File pleine')
        else:
            self.__data[self.__end % self.__taille] = x
            self.__end += 1

    def defiler(self):
        if self.est_vide():
            raise Exception("File vide")
        else:
            x = self.__data[self.__start % self.__taille]
            self.__start += 1
            return x
        
    def __repr__(self):
        res = []
        for i in range(self.__start, self.__end):
            res.append(self.__data[i % self.__taille])
        return str(res)

##################################### Exercices ################################


def enfiler(x, f: File):
    """Enfile x dans la File f"""
    ...


def pleine_ou_non(f:File):
    """Regarde si une File est pleine ou non. Renvoie True si elle est pleine"""
    ...

assert pleine_ou_non(File(5)) == False