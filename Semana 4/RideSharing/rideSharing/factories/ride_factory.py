from abc import ABC, abstractmethod
from domain.ride import Ride

class RideFactory(ABC):
    #Creador abstracto para los viajes de la plataforma
    
    @abstractmethod
    def create_ride(self, passenger):
        pass

class SharedRideFactory(RideFactory):
    #Creador concreto de viajes compartidos.

    def create_ride(self, passenger):
        return Ride(passenger)
