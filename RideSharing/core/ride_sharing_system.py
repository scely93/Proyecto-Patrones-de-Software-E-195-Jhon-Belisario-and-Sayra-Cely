class RideSharingSystem:
    #Punto central de la plataforma de Ride-Sharing.

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        #Inicializa el sistema una sola vez.
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.name = "Ride-Sharing Platform"

    def get_name(self):
        #Retorna el nombre de la plataforma.
        return self.name