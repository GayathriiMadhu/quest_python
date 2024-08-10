class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

#   def move(self):
    # print("My vehicle")

class Car(Vehicle):
  pass
#   def move(self):
    # print("My car is moving") 

class Boat(Vehicle):
  def move(self):
    print("My boat!!")

class Plane(Vehicle):
  def move(self):
    print("My plane!!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()