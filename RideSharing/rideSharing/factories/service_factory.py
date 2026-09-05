from abc import ABC, abstractmethod

from services.matching_service import MatchingService
from services.pricing_service import PricingService
from services.payment_service import PaymentService


class ServiceFactory(ABC):
    #Fábrica abstracta para crear una familia de servicios
    #relacionados con un viaje.

    @abstractmethod
    def create_matching_service(self):
        pass

    @abstractmethod
    def create_pricing_service(self):
        pass

    @abstractmethod
    def create_payment_service(self):
        pass

class RideSharingServiceFactory(ServiceFactory):
    #Fábrica concreta para la configuración básica
    #de los servicios de Ride-Sharing.

    def create_matching_service(self):
        return MatchingService()

    def create_pricing_service(self):
        return PricingService()

    def create_payment_service(self):
        return PaymentService()