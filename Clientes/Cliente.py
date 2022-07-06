from Clientes.Persona import Persona
import random
import logging

class Cliente(Persona):

    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)

    def __str__(self):
        return super().__str__()
    
    # Recargo/descuento del precio en base al metodo de pago
    def calcularPrecio(self, metodoDePago, precio):
        if metodoDePago == "efectivo":
            logging.info("Efectivo: descuento del 10%")
            return precio - ((precio/100)*10)
            
        elif metodoDePago == "tarjeta":
            logging.info("Tarjeta: recargo del 10%")
            return precio + ((precio/100)*10)

        else:
            logging.info('metodoDePago mal ingresado. Por favor, inserte "efectivo" o "debito".')

    # Suma iva al precio de lista
    def calcularIva(self, iva:int):
        logging.info(f'Aplica iva del: {iva}%')
        return iva

    # Aplica cupones de descuento
    def aplicarCupon(self):
        descuentos = ["2", "3", "5"]
        descuento = random.choice(descuentos)
        logging.info(f'Aplica descuento del {descuento}%')
        return int(descuento)
    
    # Precio final a pagar por la compra
    def calcularPrecioFinal(self, a, b, c):
        valorFinal = a + ((a/100)*b) - (a/100)*c
        return f'Precio final: {int(valorFinal)}'
