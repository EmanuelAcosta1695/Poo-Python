from abc import ABC

class Bicicleta(ABC):

    #constructor
    def __init__(self, modelo:str, color:str, año:int, rodado:int, tipo:str, cliente, valor:int):
        self._modelo = modelo
        self._color = color
        self._año = año
        self._rodado = rodado
        self._tipo = tipo
        self._cliente = cliente
        self._valor = valor

    def __str__(self) -> str:
        return (f'Modelo: {self._modelo}, Color: {self._color}, Año: {self._año}, Rodado: {self._rodado}, Tipo: {self._tipo}, Cliente: {self._cliente}, Valor de lista: {self._valor}')


    @property
    def modelo(self):         
        return self._modelo

    @property
    def color(self):
        return self._color
    
    @property
    def año(self):
        return self._año

    @property
    def rodado(self):
        return self._rodado

    @property
    def tipo(self):
        return self._tipo

    @property
    def valor(self):
        return self._valor

    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @color.setter
    def color(self, color):
        self._color = color

    @año.setter
    def año(self, año):
        self._año = año

    @color.setter
    def rodado(self, rodado):
        self._rodado = rodado

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @valor.setter
    def valor(self, valor):
        self._valor = valor

