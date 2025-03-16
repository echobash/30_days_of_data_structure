from LLD.Oops.interface_and_abc.car_interface import Car


class Mercedes(Car):
    def __init__(self,name, color):
        self.name = name
        self.color = color

    def get_name(self):
        print(f"It is {self.name}")

    def get_color(self):
        print(f"It is {self.color}")


mercedes = Mercedes("Mercedes Benz", "White")
mercedes.get_color()
mercedes.get_name()

