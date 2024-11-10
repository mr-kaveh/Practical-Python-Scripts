class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine with {} horsepower starts.".format(self.horsepower)

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start(self):
        return "{} {}: {}".format(self.make, self.model, self.engine.start())

# Create an Engine object
my_engine = Engine(horsepower=300)

# Create a Car object with the Engine object
my_car = Car(make="Ford", model="Mustang", engine=my_engine)

# Start the car
print(my_car.start())
