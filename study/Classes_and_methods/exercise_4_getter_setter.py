#getter a setter jsou způsoby OOP, které se používají pro přehlednost

class Ball():
    def __init__(self) -> None:
        self.color = 'unknown'
        self.size = 'unknown'
    
    def setColor(self, color:str):  #setter
        self.color = color

    def getColor(self):             #getter
        return self.color
    
    def setSize(self, size:str):    #setter size
        self.size = size

    def getSize(self):              #getter size
        return self.size


ball1 = Ball()
ball1.setColor('blue')
ball1.setSize('velký')
print(f'Toto je míč, který je {ball1.size} a jeho barva je {ball1.color}')
