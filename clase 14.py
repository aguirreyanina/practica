# #consigna = """
#     Consigna: Crear un sistema de gestión de estudiantes.

# Crea una clase base llamada "Estudiante" con los siguientes atributos:

# nombre: una cadena para almacenar el nombre del estudiante.
# edad: un número entero para almacenar la edad del estudiante.
# Además, implementa un método llamado "es_mayor_de_edad" que verifique si el estudiante es mayor de edad. Este método debe devolver True si el estudiante tiene 18 años o más, y False en caso contrario.

# Crea una clase derivada llamada "EstudianteUniversitario" que herede de la clase "Estudiante". Esta clase debe tener dos atributos adicionales:

# carrera: una cadena para almacenar la carrera universitaria del estudiante.
# semestre: un número entero para almacenar el semestre en el que se encuentra el estudiante.
# Sobreescríbe el método "es_mayor_de_edad" para incluir una condición adicional: si el estudiante 
# es menor de edad pero se encuentra en el tercer semestre o superior, se considerará como mayor de edad.

# Crea otra clase derivada llamada "EstudianteSecundario" que herede de la clase "Estudiante". 
# Esta clase debe tener un atributo adicional:

# colegio: una cadena para almacenar el nombre del colegio secundario del estudiante.
# Sobreescríbe el método "es_mayor_de_edad" para que siempre devuelva False, ya que los estudiantes 
# secundarios son menores de edad.

# Crea instancias de las clases "EstudianteUniversitario" y "EstudianteSecundario" y muestra la información de cada estudiante, incluyendo su nombre, edad y si es mayor de edad según la lógica implementada en cada clase.
# """

class estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    

    def mostrar_datos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad : {self.edad}")

    def es_mayor_de_edad(self):
        if self.edad > 18: print("es mayor de edad") 
        else: print("Es menor de edad")

yanina = estudiante("yanina", 24)

yanina.mostrar_datos()
yanina.es_mayor_de_edad()

class estudianteUniversitario(estudiante):
    def __init__(self, nombre, edad, carrera, semestre):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.semestre = semestre
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Carrera: {self.carrera}")
        print(f"semestre: {self.semestre}")
    
    def es_mayor_de_edad(self):
        if self.edad > 18 or self.semestre >3 : print("es mayor de edad") 
        else: print("Es menor de edad")

agregado = estudianteUniversitario("yanina", 24,"programadora", 4)
agregado.mostrar_datos()
agregado.es_mayor_de_edad()
    

