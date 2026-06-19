# 1) Animales y sonido:

# Importamos ABC y abstractmethod para crear clases abstractas
from abc import ABC, abstractmethod

# Definimos la clase base abstracta Animal
class Animal(ABC):
    # Constructor: inicializa el animal con un nombre
    def __init__(self, nombre):
        # Guardamos el nombre como atributo de instancia
        self.nombre = nombre

    # Decorador que indica que el siguiente método es abstracto
    @abstractmethod
    # Método abstracto: obliga a las subclases a implementar este método
    def hacer_sonido(self):
        pass  # No tiene implementación en la clase base

# Subclase Perro que hereda de Animal
class Perro(Animal):
    # Implementación del método hacer_sonido para el Perro
    def hacer_sonido(self):
        return f"{self.nombre} dice: Guau!"  # Retorna el sonido del perro

# Subclase Gato que hereda de Animal
class Gato(Animal):
    # Implementación del método hacer_sonido para el Gato
    def hacer_sonido(self):
        return f"{self.nombre} d
