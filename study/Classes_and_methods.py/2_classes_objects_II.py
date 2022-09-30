# můžu vytvořit nekonečno instancí a už mají definované values
class Lifeform():
    def __init__(self, purpose:str, legs:int = 2 , beauty = 'beautifull'):
        self.legs = legs
        self.purpose = purpose
        self.beauty = beauty
        self.name = self.__str__()
    
class Human(Lifeform):
    def __init__(self, purpose:str, legs:int = 2, beauty='beautifull'):
        super().__init__(purpose, legs, beauty)
        self.reputation()

    def reputation(self):
        print(f'tohle je {self.name}. Má {self.legs} nohou. Údělem této bytosti je {self.purpose} a je {self.beauty}')

haryk = Human(purpose ='be black')
hanygerka = Human(purpose = 'be bitch', beauty= 'ugly as shit')



# Nemám tušení jak udělat aby to psalo jméno toho oběktu, aniž bych té kláse vytvářel novou proměnou. Jde to vůbec?
# Asi to nejde
        
    


