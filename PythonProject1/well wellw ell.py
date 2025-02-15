class Car:
    def __init__(self):
        self.wheels = 4
        self.fuel = "бензин"

    def drive(self):
        return "Машина едет по дороге."


class Boat:
    def __init__(self):
        self.propeller = 1
        self.fuel = "дизель"

    def sail(self):
        return "Лодка плывет по воде."


class Gybrid(Car, Boat):
    def __init__(self):
        Car.__init__(self)
        Boat.__init__(self)
        self.mode = "гибрид"

    def izmena(self, mode):
        if mode == "земля":
            return "режим: колесо, машина поехала!"
        elif mode == "вода":
            return "режим: винт, лодка поплыла!"
        else:
            return "Такого режима нет"


gybrid = Gybrid()
print(gybrid.wheels)
print(gybrid.propeller)
print(gybrid.fuel)
print(gybrid.drive())
print(gybrid.sail())
print(gybrid.izmena("земля"))
print(gybrid.izmena("вода"))
