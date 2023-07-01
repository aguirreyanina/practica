""" Consigna:

Estás desarrollando un sistema para administrar una biblioteca. 
En la biblioteca existen diferentes tipos de materiales, como libros, revistas y películas. 
Cada material tiene un título, un autor y una fecha de publicación. Además, cada tipo de material 
tiene características y acciones específicas.

Debes implementar un sistema de clases que permita crear diferentes tipos de materiales con sus respectivas 
características. A continuación se detallan los requerimientos:

1. La clase base se llama "Material" y tiene los atributos: título, autor y fecha de publicación. 
También debe tener métodos para mostrar información del material y realizar una acción específica. 
(Informacion: __str__)

2. Hay tres tipos de materiales: "Libro", "Revista" y "Película". Cada tipo de material
 tiene características y acciones adicionales:

- El libro tiene un número de páginas y puede ser prestado a los usuarios.
- La revista tiene un número de edición y puede ser renovada por los usuarios.
- La película tiene una duración y puede ser reproducida en un reproductor.

3. Cada tipo de material debe ser una subclase de la clase base "Material" y debe 
sobrescribir los métodos para reflejar su comportamiento específico.

4. Implementa una clase adicional llamada "Biblioteca" que puede contener diferentes materiales. 
Debe permitir agregar materiales a la biblioteca, mostrar la información de todos los materiales en 
la biblioteca y realizar una acción conjunta, donde todos los materiales sean utilizados por los usuarios.

Tu tarea es implementar las clases mencionadas y crear instancias de materiales y una biblioteca 
para probar el funcionamiento del sistema.
"""

class material:
    def __init__(self, titulo, autor, fechaPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.fechaPublicacion = fechaPublicacion

    def __str__(self, titulo, autor, fechaPublicacion):
        return f"{self.titulo} {self.autor} {self.fechaPublicacion}"
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_fechaPublicacion(self):
        return self.fechaPublicacion

    def set_titulo(self):
        self.titulo = titulo

    def set_autor(self):
        self.autor = autor

    def set_fechaPublicacion(self):
        self.fechaPublicacion = fechaPublicacion
            
    