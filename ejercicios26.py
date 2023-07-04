# # Ejercicios de Practica:

# """
# 1- Variables:
# Pide al usuario que ingrese su nombre y luego imprime un mensaje de bienvenida utilizando esa variable.

# 2-Estructuras condicionales (if, elif, else):
# Escribe un programa que solicite al usuario ingresar un número y luego determine si es positivo, 
# negativo o cero.

# 3-Bucles (while, for):
# Utilizando un bucle while, imprime los números del 1 al 10 en orden ascendente.
# Utilizando un bucle for, imprime los números pares del 1 al 20.

# 4-Listas:
# Crea una lista de nombres de personas y luego itera sobre ella para imprimir cada nombre en una línea.

# 5-Tuplas:
# Crea una tupla de colores y luego itera sobre ella para imprimir cada color en una línea.

# 6-Diccionarios:
# Crea un diccionario con nombres de ciudades como clave y su población como valor. 
# Luego, itera sobre el diccionario e imprime el nombre de la ciudad y su población.

# 7-Programación orientada a objetos (POO):
# Crea una clase llamada "Rectángulo" con atributos de longitud y ancho. 
# Implementa métodos para calcular el área y el perímetro del rectángulo.

# 8-Método especial str:
# Modifica la clase "Rectángulo" anterior para que el método str devuelva una representación 
# legible del rectángulo.

# 9-Herencia y herencia múltiple:
# Crea una clase base llamada "Vehículo" con atributos como marca, modelo y año. 
# Luego, crea clases derivadas como "Automóvil" que tengan el atributo puertas y "Motocicleta" 
# que tengan el atributo cilindrada y que hereden de la clase base.

# 10- POO
# Crea una clase llamada Estudiante que represente a un estudiante de una institución educativa. 
# La clase debe tener los siguientes atributos:
# nombre: el nombre del estudiante.
# edad: la edad del estudiante.
# calificaciones: una lista de calificaciones del estudiante en diferentes asignaturas.

# La clase Estudiante debe tener los siguientes métodos:
# calcular_promedio(): este método calcula el promedio de las calificaciones del estudiante y
#  lo devuelve como resultado.
# obtener_estado(): este método determina si el estudiante está aprobado o reprobado. 
# Si el promedio de calificaciones es mayor o igual a 70, el estudiante se considera aprobado; 
# de lo contrario, se considera reprobado.

# Además, implementa el método especial __str__ en la clase Estudiante para que al 
# imprimir un objeto estudiante, se muestre su nombre y edad de forma legible.

# Crea una lista de estudiantes con al menos 3 instancias de la clase Estudiante, 
# cada una con diferentes nombres, edades y calificaciones. Luego, utiliza un bucle for para recorrer 
# la lista de estudiantes y mostrar la siguiente información de cada estudiante:
# Nombre y edad del estudiante.
# Promedio de calificaciones del estudiante.
# Estado (aprobado o reprobado) del estudiante, basado en su promedio de calificaciones.

# nombre = input("Ingrese su nombre: ")
# print(f"Bienvenido a python {nombre}")

# numeros = int(input("Ingrese un numero: "))
# if numeros > 0:
#     print("El numero es positivo")
# elif numeros < 0:
#     print("El numero es negativo")
# else:
#     print("El numero es 0" )

# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# for i in range (0,21,2):
#     print(i)

# nombres = ["Vanesa", "Ludmila", "Carolina", "Sofia"]
# for i in nombres:
#     print(i)

class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    def area(self):
        return self.longitud * self.ancho
    
    def perimetro (self):
        return 2* self.longitud + self.ancho

figura = Rectangulo(7,4)
print(f"El area es: {figura.area()}")

figura = Rectangulo(2,3)
print(f"El perimetro es: {figura.perimetro()}")


    


    


    
