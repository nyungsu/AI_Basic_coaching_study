class Car:
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels


class Bike(Car):
    def __init__(self, fuel, wheels, size):
        # fuel, wheels는 부모클래스 꺼 그대로
        super().__init__(fuel, wheels)
        self.size = size
    


bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)
