from abc import ABC, abstractmethod

class Persona(ABC):

    #constructor
    def __init__(self, id, nombre, apellido, edad):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def __str__(self) -> str:
        return (f'Id: {self._id}, Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}')


    @property
    def id(self):          # <--- el get y set se tienen que llamar igual
        return self._id

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad


    @id.setter
    def id(self, id):
        self._modelo = id

    @nombre.setter
    def nombre(self, nombre):
        self._color = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._año = apellido

    @edad.setter
    def edad(self, edad):
        self._rodado = edad
    

    @abstractmethod
    def calcularPrecio(self, metodoDePago):
        pass

    @abstractmethod
    def calcularIva(self, iva:int):
        pass

    @abstractmethod
    def aplicarCupon(self):
        pass

    @abstractmethod
    def calcularPrecioFinal(self):
        pass