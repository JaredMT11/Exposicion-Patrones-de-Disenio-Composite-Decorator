from .component import Notificacion

class MensajeSimple(Notificacion):
    def __init__(self, texto: str):
        self._texto = texto

    def contenido(self) -> str:
        return self._texto