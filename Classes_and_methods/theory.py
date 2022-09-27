from curses import init_color


# Konstruktor, alokátor, initor
# konstruktor = třída volaná, jako funkce
# Vytvoření instance:   __new__()       alokátor
#                       __init__()      initor
#__new__()  alokuje/ vyhradí pro nový objekt místo v paměti
#__init__() metoda polotovar inicializuje ...



# Definice třídy (class)
# Velblboudí notace

# class NazevTridy:
# Datové atributy:  Pro všechny instance společný
# Metody:           Instanční:  
#                   Statické:   
# Instanční: schopnosti instancí; počáteční parametr "self"; 
# Statické:  pracuje pro metodu; nepotřebuje parametr instance/třídy (self); 


class ExerciseClass:
    """tato třída je první pokus o pochopení tříd a metod
    """
    def __init__(self) -> None:         #initor třídy 
        pass
    
    