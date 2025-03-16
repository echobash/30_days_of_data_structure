class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Color - {self.color}")
        print(f"Car Make - {self.make}")
        print(f"Car Model - {self.model}")
        print(f"Car Year - {self.year}")


car = Car('Red', 'Tata', 'Indica', 2000)
car2 = Car('Black', 'Mahindra', 'Thar', 2004)
car.display_info()
print("-----------")
car2.display_info()