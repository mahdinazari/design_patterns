from abc import ABC, abstractmethod


# Product
class Delivery(ABC):
    @abstractmethod
    def deliver(self) -> str:
        raise NotImplementedError


# Concrete Product1
class GroundDelivery(Delivery):
    def deliver(self) -> str:
        return "Delivering by ground transportation"


# Concrete Product2
class AirDelivery(Delivery):
    def deliver(self) -> str:
        return "Delivering by air transportation"


# Creator
class DeliveryCreator(ABC):
    @abstractmethod
    def factory_method(self) -> Delivery:
        raise NotImplementedError
    
    def process_delivery(self) -> str:
        delivery = self.factory_method()
        return f"Delivery started: {delivery.deliver()}"

# Concrete Creator
class GroundDeliveryCreator(DeliveryCreator):
    def factory_method(self) -> Delivery:
        return GroundDelivery()


# Concrete Creator
class AirDeliveryCreator(DeliveryCreator):
    def factory_method(self) -> Delivery:
        return AirDelivery()


def client_code(creator: DeliveryCreator):
    print(creator.process_delivery())

if __name__ == "__main__":
    print("Testing Ground Delivery:")
    client_code(GroundDeliveryCreator())
    
    print("Testing Air Delivery:")
    client_code(AirDeliveryCreator())
