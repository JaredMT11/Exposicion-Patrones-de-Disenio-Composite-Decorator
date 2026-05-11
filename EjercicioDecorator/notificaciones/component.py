from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def contenido(self) -> str:
        pass