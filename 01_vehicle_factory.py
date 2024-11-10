from abc import ABC, abstractmethod
from log import logger


# abstract Vehicle class
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


# Car class inheriting from Vehicle parent class
class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Engine started")


# Motorcycle class inheriting from Vehicle parent class
class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.spec} Spec): Motor started")


# abstract VehicleFactory class
class VehicleFactory(ABC):
    def __init__(self, spec):
        self.spec = spec

    @abstractmethod
    def create_car(self, make, model) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Motorcycle:
        pass


# US-specific VehicleFactory implementation
class USVechicleFactory(VehicleFactory):
    def __init__(self):
        super().__init__("US")

    def create_car(self, make, model) -> Car:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, self.spec)


# EU-specific VehicleFactory implementation
class EUVehicleFactory(VehicleFactory):
    def __init__(self):
        super().__init__("EU")

    def create_car(self, make, model) -> Car:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, self.spec)


# create US vehicle factory
us_vehicle_factory = USVechicleFactory()

# create EU vehicle factory
eu_vehicle_factory = EUVehicleFactory()

# create US car
vechicle1 = us_vehicle_factory.create_car("Ford", "Mustang")
vechicle1.start_engine()

# create EU motorcycle
vehicle2 = eu_vehicle_factory.create_motorcycle("BMW", "S1000RR")
vehicle2.start_engine()
