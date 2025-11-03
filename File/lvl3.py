from lvl1 import File

############################################################################################

def combiner(f1: File, f2: File) -> File:
    """Combine deux file et les classe dans le bon ordre (croissant)"""
    rendu = ... #Une File vide
    liste1 = []
    liste2 = []
    while ...: #Tant qu'il reste des éléments dans f1
        ... #On défile tout les éléments de f1 et on les mets dans liste1
    while ...: #Tant qu'il reste des éléments dans f2
        ... #On défile tout les éléments de f2 et on les mets dans liste2
    liste3 = ... #On met liste1 et liste2 dans liste3
    liste3 = sorted(...) #Ont tri de manière croissante la liste avec la méthode sorted()
    for k in ...:
        ... #On enfile tout les éléments de liste3 dans rendu
    return ...

############################################################################################