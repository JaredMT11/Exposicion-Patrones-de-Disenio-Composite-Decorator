from .component import Notificacion

class DecoradorBase(Notificacion):
    def __init__(self, notif: Notificacion):
        self._notif = notif

    def contenido(self) -> str:
        return self._notif.contenido()