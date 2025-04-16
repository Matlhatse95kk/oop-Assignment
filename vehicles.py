class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving on the road!"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky!"

class Boat(Vehicle):
    def move(self):
        return "Sailing on water!"

# Example usage:
def demonstrate_movement(vehicle):
    print(vehicle.move())

car = Car()
plane = Plane()
boat = Boat()

demonstrate_movement(car)   # Output: Driving on the road!
demonstrate_movement(plane) # Output: Flying in the sky!
demonstrate_movement(boat)  # Output: Sailing on water!