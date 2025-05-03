class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        # self.total_car += 1  //Can do this too

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



ElectricCar("Tesla", "Model S", "85kWH")


Car("Toyota", "Corolla")


# my_new_car = Car("Tata", "Harrier")
# print(my_new_car.model)

print(Car.total_car)