from lvl1 import File

############################################################################################

def inverser(f: File) -> File:
    """Inverse une File f"""
    pile = []
    while ...: #Tant qu'il reste des éléments dans f
        pile.append(...)

    while ... > ...: #Tant qu'il reste des éléments dans pile
        f.enfiler(...) #On renfile le dernier élément de pile (indice : pop())

    return f
    
############################################################################################

def copier(f: File) -> File:
    """Copie une File f sans la modifier. La File f ne sera pas plus grande que 100"""
    copie = File(100)
    temporaire = File(100)
    while ...: #Tant qu'il reste des éléments dans f
        x = f.defiler()
        ... #On ajoute a copie 'x'
        ... #On ajoute a temporaire 'x'

    while ...: #Tant qu'il reste des éléments dans temporaire
        f.enfiler(...) #On remet les valeur de temporaire dans f
        
    return copie
    
############################################################################################