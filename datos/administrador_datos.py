# datos/administrador_datos.py
class DataManager:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita):
        self.citas.append(cita)
        return "--------------------------------\nCita agregada correctamente.\n--------------------------------"

    def obtener_citas(self):
        return self.citas

    def eliminar_cita(self, fecha_cita):
        self.citas = [cita for cita in self.citas if cita["date_time"] != fecha_cita]
        return "--------------------------------\nCita eliminada correctamente.\n--------------------------------"