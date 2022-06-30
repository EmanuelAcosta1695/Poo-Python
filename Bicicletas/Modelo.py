from Bicicletas.Bicicleta import Bicicleta

class Modelo(Bicicleta):

    def __init__(self, modelo: str, color: str, año: int, rodado: int, tipo: str, cliente, valor: int):
        super().__init__(modelo, color, año, rodado, tipo, cliente, valor)

    def __str__(self) -> str:
        return super().__str__()
