from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class RealDelivery(Delivery):
    def __init__(self):
        print("Initializing RealDelivery (expensive operation)")
    
    def deliver(self) -> str:
        return "Delivering package via real system"


class DeliveryProxy(Delivery):
    def __init__(self):
        self._real_delivery = None 
    
    def deliver(self) -> str:
        if self._real_delivery is None:
            self._real_delivery = RealDelivery()
        return self._real_delivery.deliver()


def client_code(delivery: Delivery):
    print(delivery.deliver())


if __name__ == "__main__":
    print("Using Delivery Proxy:")
    proxy = DeliveryProxy()
    client_code(proxy)
    
    print("\nCalling again (RealDelivery already initialized):")
    client_code(proxy)
    