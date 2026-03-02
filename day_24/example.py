class Car:
  def __init__(self, model, year, brand, color, oil_level=100, performance=0.1):
    self.model = model
    self.year = year
    self.brand = brand
    self.color = color
    self.distance = 0
    self.oil_level = oil_level
    self.performance = performance

  def travel(self, a, b):
    self.distance += (b - a)
    self.oil_level -= (b - a) * self.performance

  def current_oil_level(self):
    return self.oil_level


car1 = Car("Model S", 2020, "Tesla", "Red",500)

print(car1.current_oil_level())  # Output: 500.0

print(car1.model)  # Output: Model S
print(car1.year)   # Output: 2020
print(car1.brand)  # Output: Tesla    
print(car1.color)  # Output: Red

car1.travel(10, 100)
print(car1.distance)  # Output: 100
car1.travel(100, 150)
print(car1.distance)  # Output: 150


car2 = Car("Mustang", 2018, "Ford", "Blue")

print(car2.current_oil_level())  # Output: 100.0

print(car2.model)  # Output: Mustang
print(car2.year)   # Output: 2018
print(car2.brand)  # Output: Ford
print(car2.color)  # Output: Blue

car2.travel(0, 50)
print(car2.distance)  # Output: 50
car2.travel(50, 120)
print(car2.distance)  # Output: 120

print(car1.current_oil_level())  # Output: 85.0
print(car2.current_oil_level())  # Output: 93.0
