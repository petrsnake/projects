from curses import init_color
from re import S
from unittest import makeSuite


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
    def __init__(self) -> None: 
        #initor třídy 
        """
        tato funkce se spusti pokazde kdyz tridu nejak inicializues..
        proto se nazyva init..
        napr:
        myclass = ExerciseClass() by spustilo tuto funkci.. vyuziti nize
        """
        pass
    

class Animal:
    def __init__(self, animal_name: str, make_sound: int = 1) -> None:
        self.animal_name = animal_name # inicializuju si promenou v tride
        self.make_sound = make_sound

        if self.animal_name == "cat":
            for i in range(self.make_sound):
                print ("meow")
        elif self.animal_name == "dog":
            for i in range(self.make_sound):
                print ("bark")

    ###_________ na dalsi metodu teto classy koukni az pochopis to co je nahore
    
    def take_a_shit(self): # self pridava metode VSECHNY variables teto classy
        print (f"{self.animal_name} is taking a shit")

# ted ji jdu inicializovat
# spust tento program
dog_animal = Animal("dog", 1) # zde jde o psa a zasteka 1x
cat_animal = Animal("cat", 3) # zde o kocku a zamnouka 3x

# - az pochopis to co je nad timto tak
# odkomentuj to co je nize a spust znovu 
# dog_animal.take_a_shit()
# cat_animal.take_a_shit()
    