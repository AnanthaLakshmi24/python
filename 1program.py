class Human:
    def __init__(self):
        self.x=0
        self.y=0
        print("Hai")
    def Increment(self):
        self.x=self.Givevalue()+1
    def Givecalue(self):
        return self.y
thub=Human()
thub.Increment()
print(thub.x)
