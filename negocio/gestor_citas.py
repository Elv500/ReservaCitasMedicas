# negocio/gestor_citas.py
from datos.administrador_datos import DataManager
from negocio.fabrica_doctores import DoctorFactory
from negocio.notificador import Notificador, EmailNotifier, SMSNotifier, LoggingNotifierDecorator

class GestorCitas:
    def __init__(self):
        self.admin_datos = DataManager()
        self.observadores = [
            LoggingNotifierDecorator(EmailNotifier()),
            LoggingNotifierDecorator(SMSNotifier())
        ]

    def agendar_cita(self, nombre_paciente, tipo_doctor, especialidad, fecha_cita):
        doctor = DoctorFactory.crear_doctor(tipo_doctor, "Dr. " + tipo_doctor, especialidad)
        cita = {"patient_name": nombre_paciente, "doctor_name": doctor.nombre, "date_time": fecha_cita}
        mensaje_agregar = self.admin_datos.agregar_cita(cita)
        self.notificar(f"Cita agendada para {nombre_paciente} con {doctor.nombre} el {fecha_cita}")
        return f"{mensaje_agregar}\nCita agendada para {nombre_paciente} con {doctor.nombre} el {fecha_cita}"

    def notificar(self, mensaje):
        for observador in self.observadores:
            observador.enviar_notificacion(mensaje)

    def obtener_citas(self):
        return self.admin_datos.obtener_citas()

    def cancelar_cita(self, fecha_cita):
        return self.admin_datos.eliminar_cita(fecha_cita)