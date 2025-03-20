from abc import ABC, abstractmethod


class Delivery(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class OldDeliverySystem:
    def ship(self) -> str:
        return "Shipping via old system"


class DeliveryAdapter(Delivery):
    def __init__(self, old_system: OldDeliverySystem):
        self.old_system = old_system
    
    def deliver(self) -> str:
        return self.old_system.ship().replace("Shipping", "Delivering")


def client_code(delivery: Delivery):
    print(delivery.deliver())


if __name__ == "__main__":
    old_delivery = OldDeliverySystem()
    adapted_delivery = DeliveryAdapter(old_delivery)
    
    print("Using adapted old delivery system:")
    client_code(adapted_delivery)
    
    class ModernDelivery(Delivery):
        def deliver(self) -> str:
            return "Delivering via modern system"
    
    print("Using modern delivery system:")
    client_code(ModernDelivery())
