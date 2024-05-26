# negocio/notificador.py
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje):
        pass

class EmailNotifier(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por email:\n  {mensaje}")

class SMSNotifier(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por SMS:\n  {mensaje}")

class LoggingNotifierDecorator(Notificador):
    def __init__(self, notificador):
        self._notificador = notificador

    def enviar_notificacion(self, mensaje):
        # Registro del mensaje antes de enviarlo
        print(f"Registrando mensaje: {mensaje}")
        self._notificador.enviar_notificacion(mensaje)