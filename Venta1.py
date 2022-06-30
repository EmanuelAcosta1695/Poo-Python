#%%
from asyncio.log import logger
from Bicicletas.Modelo import Modelo
from Clientes.Cliente import Cliente
import logging

logging.basicConfig(filename='H:\\EMA\\VISUAL\\Poo\\TpFede\\logs\\venta.log', encoding='utf-8', level=logging.INFO)


persona1 = Cliente(1, "Juan", "Garcia", 32)
mountainBike = Modelo("Sunshine", "Negro", 2022, 29, "mountainBike", persona1, 50000)

logger.info(" ")
logger.info(mountainBike) 

valor = mountainBike.valor

recargo = persona1.calcularPrecio("efectivo", valor)
iva = persona1.calcularIva(21)
cupon = persona1.aplicarCupon()

logger.info(persona1.calcularPrecioFinal(recargo, iva, cupon))

# %%
