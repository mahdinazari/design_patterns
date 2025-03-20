class Warehouse:
    def prepare_package(self) -> str:
        return "Package prepared in warehouse"


class Transport:
    def ship_package(self) -> str:
        return "Package shipped via transport"


class Notification:
    def send_notification(self) -> str:
        return "Notification sent to customer"


class DeliveryFacade:
    def __init__(self):
        self.warehouse = Warehouse()
        self.transport = Transport()
        self.notification = Notification()
    
    def deliver_package(self) -> str:
        result = []
        result.append(self.warehouse.prepare_package())
        result.append(self.transport.ship_package())
        result.append(self.notification.send_notification())
        return "\n".join(result)


def client_code(facade: DeliveryFacade):
    print(facade.deliver_package())


if __name__ == "__main__":
    delivery_facade = DeliveryFacade()
    print("Delivering package using Facade:")
    client_code(delivery_facade)
