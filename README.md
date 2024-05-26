Arquitectura de Software 1-2024 UMSS
Estudiante: Elvis Alvarez Cayo

Requerimientos:
- Python 3.12.2
- IDE (Ejm:VSCode)

Para poder ejecutar el programa, solo es necesario clonar/descargar este repositorio en su equipo.
Y finalmente ejecutar el archivo main.py

--------------------------------------
Proyecto:
--------------------------------------

El sistema de reserva de citas médicas permite a los pacientes programar citas con diferentes tipos de doctores (médicos generales y especialistas) y recibir notificaciones por correo electrónico o SMS sobre las citas programadas. Además agregando las funciones de visualizar y eliminar las citas agendadas.

--------------------------------------
Principios SOLID
--------------------------------------

-Single Responsibility Principle (SRP):
  DataManager se encarga exclusivamente de la gestión de los datos de las citas.
  GestorCitas maneja la lógica de negocio relacionada con la programación de citas y la coordinación de notificaciones.
  Las clases de notificación (EmailNotifier, SMSNotifier) se centran en enviar notificaciones a través de un medio específico.

-Open/Closed Principle (OCP):
  Puedes añadir más tipos de doctores y notificadores sin modificar el código existente, extendiendo las clases base (Doctor, Notificador) y usando decoradores para añadir funcionalidades sin alterar el comportamiento de las clases existentes.

-Liskov Substitution Principle (LSP):
  Las subclases de Notificador pueden ser intercambiadas sin afectar el comportamiento esperado del sistema, cumpliendo con LSP.

-Interface Segregation Principle (ISP):
  Notificador provee una interfaz simple con un único método que las clases concretas deben implementar, evitando que estas clases implementen métodos que no necesitan.

-Dependency Inversion Principle (DIP):
  GestorCitas depende de abstracciones (DataManager, Notificador), no de implementaciones concretas, lo que facilita la sustitución de componentes y mejora la flexibilidad.

--------------------------------------
Patrones de Diseño
--------------------------------------

-Factory Method(Patrón Creacional):
  Utilizado en DoctorFactory para crear instancias de Doctor. Este patrón permite la creación de diferentes tipos de doctores sin especificar las clases concretas en la capa de negocio.

-Decorator(Patrón Estructural):
  LoggingNotifierDecorator es un ejemplo clásico del patrón Decorator, añadiendo funcionalidades de registro a los notificadores existentes sin modificar su comportamiento original.

-Observer(Patrón de Comportamiento):
  GestorCitas actúa como un sujeto que notifica a varios observadores (notificadores decorados) cuando se programa una nueva cita. Cada notificador, ahora observador, se activa en respuesta a este evento.

--------------------------------------
Arquitectura de Tres Capas
--------------------------------------

-Capa de Presentación:
  La interfaz de usuario (InterfazUsuario) se encarga de todas las interacciones con el usuario, solicitando datos y mostrando información.

-Capa de Negocio:
  GestorCitas, junto con DoctorFactory y Notificador (incluyendo sus decoradores), manejan la lógica de negocio, como la gestión de citas y notificaciones.

-Capa de Datos:
  DataManager maneja la persistencia y manipulación de datos relacionados con las citas, actuando como el único punto de contacto para la gestión de datos dentro del sistema.
