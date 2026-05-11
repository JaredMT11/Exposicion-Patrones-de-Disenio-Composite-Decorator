from ..decorator import DecoradorBase

class DecoradorUrgente(DecoradorBase):
    def contenido(self) -> str:
        return "[URGENTE] " + self._notif.contenido()