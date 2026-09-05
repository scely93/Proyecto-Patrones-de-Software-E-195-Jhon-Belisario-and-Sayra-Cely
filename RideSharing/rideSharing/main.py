#Jhon Belisario - Sayra Cely
from core.ride_sharing_system import RideSharingSystem

from domain.passenger import Passenger
from domain.driver import Driver

from factories.ride_factory import SharedRideFactory
from factories.service_factory import RideSharingServiceFactory


def main():

    #SINGLETON

    system_1 = RideSharingSystem()
    system_2 = RideSharingSystem()

    print("SINGLETON")
    print("-----------------------------------------")
    print(system_1.get_name())

    print("¿Es la misma instancia?")
    print(system_1 is system_2)

    print("\n=========================================")

    #ACTORES DEL RIDE-SHARING

    passenger = Passenger("Pasajero 1")
    driver = Driver("Conductor 1")

    #FACTORY METHOD

    print("FACTORY METHOD")
    print("-----------------------------------------")

    ride_factory = SharedRideFactory()
    ride = ride_factory.create_ride(passenger)

    print(ride.get_description())
    print("\n=========================================")

    #ABSTRACT FACTORY

    print("ABSTRACT FACTORY")
    print("-----------------------------------------")

    service_factory = RideSharingServiceFactory()

    matching_service = service_factory.create_matching_service()
    pricing_service = service_factory.create_pricing_service()
    payment_service = service_factory.create_payment_service()

    # Coincidencia entre pasajero y conductor
    matching_result = matching_service.match(
        passenger,
        driver
    )

    print(matching_result)

    # Asignamos el conductor al viaje
    ride.assign_driver(driver)
    print(ride.get_description())

    # Cálculo de tarifa
    price = pricing_service.calculate_price(10)
    print(f"Tarifa para 10 km: ${price}")

    # Registro del pago
    payment_result = payment_service.process_payment(price)
    print(payment_result)

if __name__ == "__main__":
    main()

