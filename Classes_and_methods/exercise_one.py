# První programování class

class Website:
    def __init__(self, title:str):
        self.title = title

    def showName(self):
        print(self.title)

web1 = Website('www.python.cz')
web1.showName()


# classa s barvami

class Colors:
    def __init__(self, color:str, darknes:bool):
        self.color = color
        self.darkness = darknes

    def __str__(self):
        return f'Objekt {self} má barvu {self.color}. Je tmavý {self.darkness}'
    
    def ShitTalk(self):
        print(str(self.__str__))

modra = Colors('modrá', True)
zluta = Colors('žlutá', False)

modra.ShitTalk()    # Proč to nevypíše tu větu z metody __str__()? 
