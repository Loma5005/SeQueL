class EmobilisStudent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and i'm {self.age} years old")
#creating an object
myobj=EmobilisStudent("Timothy",22)
myobj.hello_me()

class EmobilisEmployee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and i'm {self.age} years old")
myobj=EmobilisEmployee("Jane",32)
myobj.hello_me()

class CarsEmporiumOwner:
    def __init__(self,  name, age):
        self.name = name
        self.age = age
    def hello_me(self):
        print(f"My name is {self.name} and i'm {self.age} years old")
myobj=CarsEmporiumOwner("Rufus",72)
myobj.hello_me()

#create a class called magari, it should have model , year, properties
#create a minimum of 3 objects

class Magari:
    def __init__(self,model,year,properties):
        self.model=model
        self.year=year
        self.properties=properties
    def my_cars(self):
        print(f"My car is a {self.model}, manufactured in {self.year} and runs on a {self.properties}")
myobj=Magari("Bugatti Chiron Profilee",2023,"8-litre W16 powertrains")
myobj.my_cars()
myobj=Magari("Bugatti Mistral",2023,"8-litre W16 powertrains running at a top speed of 420km/h")
myobj.my_cars()
myobj=Magari("Bugatti Centodieci",2023,"8-litre W16 powertrains to produce 1600 ps")
myobj.my_cars()

