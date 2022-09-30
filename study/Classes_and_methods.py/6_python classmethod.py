# Classmethod je metoda sdílená mezi všemi objekty
# Při volání se jméno classy píše jako první argument

class Fruit:
    name = 'Fruitas'

    @classmethod
    def printName(cls):
        print('The name is:',cls.name)

apple = Fruit()
berry = Fruit()

# @classmethod ignoruje změnu parametru pro instanci
apple.name = 'apple'    
Fruit.printName()
apple.printName()
berry.printName()

# @classmethod lze změnit parametr pouze pro celou classu
Fruit.name = 'apple'
Fruit.printName()
apple.printName()
berry.printName()

# @classmethod a @staticmethod
# @classmethod ví o classe, atributech a parametrem je vždy classa
# @stathicmethod neví o classe, atributech a může být volaná jako funkce()

