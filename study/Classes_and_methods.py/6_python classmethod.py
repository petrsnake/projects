# Classmethod je metoda sdílená mezi všemi objekty
# Při volání se jméno classy píše jako první argument

class Fruit:
    name = 'Fruitas'

    @classmethod
    def printName(cls):
        print('The name is:',cls.name)

apple = Fruit()
berry = Fruit()

Fruit.printName()
apple.printName()
berry.printName()

