# clasy mohou dědit od mateřských class metody a variables
# mateřská (také: parents, super)

class Drink():
    def __init__(self) -> None:
        pass

    def setVolume(self, volume:int):
        self.volume = volume

    def getVolume(self):
        return self.volume

subjekt = Drink()
subjekt.setVolume(250)
print(subjekt.getVolume())


class Cold():                           #Proč se při spuštění inicializace classy Juice nespustí i tady ten print?
    def __init__(self) -> None:
        print('I am cold as ice')
        


class Juice(Drink, Cold):
    def __init__(self) -> None:
        super().__init__()

    def setFruit(self, fruit:str):
        self.fruit = fruit

    def getFruit(self):
        return self.fruit

subjekt2 = Juice()
subjekt2.setVolume(250)
subjekt2.setFruit('apple')
print(f'nápoj má {subjekt2.getVolume()} ml a je vyroben z {subjekt2.getFruit()}')

