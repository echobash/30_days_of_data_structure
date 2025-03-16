from LLD.Oops.interface_and_abc.car_interface import Car


class Audi(Car):
    def __init__(self,name, color):
        self.name = name
        self.color = color

    def get_name(self):
        print(f"It is {self.name}")

    def get_color(self):
        print(f"It is {self.color}")


audi = Audi("Audi A6", "Green")
audi.get_color()
audi.get_name()

