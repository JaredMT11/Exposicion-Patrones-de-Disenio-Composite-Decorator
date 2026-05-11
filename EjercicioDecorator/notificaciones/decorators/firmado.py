from ..decorator import DecoradorBase

class DecoradorFirmado(DecoradorBase):
    def __init__(self, notif, firma: str):
        super().__init__(notif)
        self._firma = firma

    def contenido(self) -> str:
        return self._notif.contenido() + f" — {self._firma}"