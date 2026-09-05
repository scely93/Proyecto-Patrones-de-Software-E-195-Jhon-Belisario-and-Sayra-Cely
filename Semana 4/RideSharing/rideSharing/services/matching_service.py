class MatchingService:
    #Servicio base para realizar la coincidencia
    #entre pasajeros y conductores.

    def match(self, passenger, driver):
        return (
            f"Coincidencia realizada: "
            f"{passenger.get_name()} - {driver.get_name()}"
        )