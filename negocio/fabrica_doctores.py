# negocio/fabrica_doctores.py
from abc import ABC, abstractmethod

class Doctor(ABC):
    @abstractmethod
    def revisar(self, nombre_paciente):
        pass

class GeneralPractitioner(Doctor):
    def __init__(self, nombre):
        self.nombre = nombre

    def revisar(self, nombre_paciente):
        return f"Dr. {self.nombre} está revisando al paciente {nombre_paciente}"

class Specialist(Doctor):
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def revisar(self, nombre_paciente):
        return f"Dr. {self.nombre} ({self.especialidad}) está consultando al paciente {nombre_paciente}"

class DoctorFactory:
    @staticmethod
    def crear_doctor(tipo_doctor, nombre, especialidad=None):
        if tipo_doctor == "GeneralPractitioner":
            return GeneralPractitioner(nombre)
        elif tipo_doctor == "Specialist":
            return Specialist(nombre, especialidad)
        else:
            raise ValueError("Tipo de doctor no soportado")
