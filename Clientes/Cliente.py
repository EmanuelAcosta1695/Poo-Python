from asyncio.log import logger
from Clientes.Persona import Persona
import random


class Cliente(Persona):

    # logging.basicConfig(filename='logs/venta.log', encoding='utf-8', level=logging.INFO)

    def __init__(self, id, nombre, apellido, edad):
        super().__init__(id, nombre, apellido, edad)

    def __str__(self):
        return super().__str__()

    def calcularPrecio(self, metodoDePago, precio):
        if metodoDePago == "efectivo":
            logger.info("Efectivo: descuento del 10%")
            return precio - ((precio/100)*10)
            
        elif metodoDePago == "tarjeta":
            logger.info("Tarjeta: recargo del 10%")
            return precio + ((precio/100)*10)

        else:
            logger.info('metodoDePago mal ingresado. Por favor, inserte "efectivo" o "debito".')


    def calcularIva(self, iva:int):
        logger.info(f'Aplica iva del: {iva}')
        return iva


    def aplicarCupon(self):
        descuentos = ["2", "3", "5"]
        descuento = random.choice(descuentos)
        logger.info(f'Aplica descuento del {descuento}%')
        return int(descuento)
    

    def calcularPrecioFinal(self, a, b, c):
        valorFinal = a + ((a/100)*b) - (a/100)*c
        return f'Precio final: {int(valorFinal)}'
