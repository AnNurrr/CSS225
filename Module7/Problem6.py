# Ainur
# 11/13/23
# Demonstrates the usage of the class by creating two car objects
# with different specifications and prints various attributes

class Car:
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.car_type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.manufacturer} {self.model} {str(self.year)} {self.color} ({self.car_type})"

# Example
car1 = Car("Sports", 2012, "Blue", "Convertible", "ExampleManufacturer")
car2 = Car("Sedan", 2020, "Black", "SedanType", "AnotherManufacturer")

print(car1.get_color())
print(car1.get_model())
print(car1.get_type())
print(car1.get_manufacturer())
print(car1.fullspecs())

print(car2.get_color())
print(car2.get_model())
print(car2.get_type())
print(car2.get_manufacturer())
print(car2.fullspecs())
