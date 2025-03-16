from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def deliver(self) -> str:
        raise NotImplementedError


class GroundDelivery(Delivery):
    def deliver(self) -> str:
        return "Delivering by ground"
    

class AirDelivery(Delivery):
    def deliver(self) -> str:
        return "Delivering by air"


class Vehicle(ABC):
    @abstractmethod
    def get_vehicle(self) -> str:
        raise NotImplementedError


class PlaneVehicle(Vehicle):
    def get_vehicle(self) -> str:
        return "Using a plane"


class TruckVehicle(Vehicle):
    def get_vehicle(self) -> str:
        return "Using a truck"


class DeliveryFactory(ABC):
    @abstractmethod
    def create_delivery(self) -> Delivery:
        raise NotImplementedError
    
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        raise NotImplementedError


class GroundDeliveryFactory(DeliveryFactory):
    def create_delivery(self) -> Delivery:
        return GroundDelivery()
    
    def create_vehicle(self) -> Vehicle:
        return TruckVehicle()


class AirDeliveryFactory(DeliveryFactory):
    def create_delivery(self) -> Delivery:
        return AirDelivery()
    
    def create_vehicle(self) -> Vehicle:
        return PlaneVehicle()


def client_code(factory: DeliveryFactory):
    delivery = factory.create_delivery()
    vehicle = factory.create_vehicle()
    print(f"{delivery.deliver()} - {vehicle.get_vehicle()}")

if __name__ == "__main__":
    print("Ground Delivery Family:")
    client_code(GroundDeliveryFactory())
    
    print("Air Delivery Family:")
    client_code(AirDeliveryFactory())
    