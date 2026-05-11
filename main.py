from notificaciones import MensajeSimple
from notificaciones.decorators import DecoradorUrgente, DecoradorFirmado

notif = MensajeSimple("Servidor caido en produccion")
notif = DecoradorUrgente(notif)
notif = DecoradorFirmado(notif, "DevOps Team")

print(notif.contenido())