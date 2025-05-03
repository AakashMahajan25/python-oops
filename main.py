class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWH")
print(my_tesla.fuel_type())


my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())

# my_new_car = Car("Tata", "Harrier")
# print(my_new_car.model)