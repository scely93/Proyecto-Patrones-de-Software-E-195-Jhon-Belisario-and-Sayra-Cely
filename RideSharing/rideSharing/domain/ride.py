class Ride:
    #Representa un viaje compartido entre pasajero y un conductor

    def __init__(self, passenger):
        self.passenger = passenger
        self.driver = None
        self.status = "Pendiente"

    def assign_driver(self, driver):
        self.driver = driver
        self.status = "Conductor asignado"

    def get_description(self):
        if self.driver is None:
            return (
                f"Viaje de {self.passenger.get_name()} - "
                f"{self.status}"
            )
        return (
            f"Viaje de {self.passenger.get_name()} "
            f"conductor: {self.driver.get_name()} - "
            f"{self.status}"
        )