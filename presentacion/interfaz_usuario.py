# presentacion/interfaz_usuario.py
from negocio.gestor_citas import GestorCitas

class InterfazUsuario:
    def __init__(self):
        self.gestor_citas = GestorCitas()

    def iniciar(self):
        print("--------------------------")
        print("Bienvenido al Sistema de Reserva de Citas Médicas")
        print("--------------------------\n")
        
        while True:
            print("1. Programar nueva cita")
            print("2. Ver todas las citas")
            print("3. Cancelar una cita")
            print("4. Salir\n\n--------------------------------")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.programar_cita()
            elif opcion == "2":
                self.ver_citas()
            elif opcion == "3":
                self.cancelar_cita()
            elif opcion == "4":
                print("\nGracias por utilizar el sistema.\n")
                break

    def programar_cita(self):
        nombre_paciente = input("Nombre del paciente: ")
        tipo_doctor = input("Tipo de doctor (GeneralPractitioner/Specialist): ")
        if tipo_doctor == "Specialist":
            especialidad = input("Especialidad: ")
        else:
            especialidad = None
        
        fecha_cita = input("Fecha y hora de la cita (DD-MM-YY HH:MM): ")
        resultado = self.gestor_citas.agendar_cita(nombre_paciente, tipo_doctor, especialidad, fecha_cita)
        print(resultado)

    def ver_citas(self):
        citas = self.gestor_citas.obtener_citas()
        if citas:
            print("Citas Programadas:")
            for cita in citas:
                print(f"- {cita['patient_name']} con {cita['doctor_name']} el {cita['date_time']}")
        else:
            print("No hay citas programadas.")

    def cancelar_cita(self):
        fecha_cita = input("Ingrese la fecha y hora de la cita a cancelar (DD-MM-YY HH:MM): ")
        resultado = self.gestor_citas.cancelar_cita(fecha_cita)
        print(resultado)