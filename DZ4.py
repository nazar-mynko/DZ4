class Didys:
    age = "70"
    ogorodov = "2"
    sosedov = "12"
class Batki(Didys):
    car = "Shevrolet"
    mobile = "Redmi"
class Dutuna(Batki):
    def __init__(self):
        print(self.age)
        print(self.ogorodov)
        print(self.sosedov)
        print(self.car)
        print(self.mobile)
nick = Dutuna()
