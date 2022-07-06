from Bicicletas.Modelo import Modelo
from Clientes.Cliente import Cliente
from Bicicletas.Stock import Stocks
import logging

logging.basicConfig(filename='H:\\EMA\\VISUAL\\Poo\\TpFede\\logs\\venta.log', encoding='utf-8', level=logging.INFO)

# cargar datos del cliente
def definirDatosCliente():
    try:
        nombre = str(input("Inserte Nombre del cliente: "))
        apellido = str(input("Inserte Apellido del cliente: "))
        edad = int(input("Inserte Edad del cliente: "))

        persona = Cliente(nombre, apellido, edad)
        logging.info(persona)

        return persona

    except Exception as e:
        logging.warning(f'Ingreso un dato erroneo: {e}. Intente nuevamente')
        definirDatosCliente()
    

# eleccion de bicicleta a comprar
def choisegBike():
    try:
        logging.info(f'Modelos disponibles: {[bike for bike in Stocks.stockBikes.items()]}')
        choice = (input("Que modelo desea elegir?: ")).lower()
        logging.info(f'Eligio: {Stocks.stockBikes[choice]}')

        return choice

    except Exception as e:
        logging.warning(f'El valor ingresado es erroneo {e}. Intente nuevamente')
        choisegBike()

   

# accion de venta + calculo de preico final
def venta():
    cliente = definirDatosCliente()
    choice = choisegBike()

    # modelo, color, año, rodado, tipo, datos del Cliente, precio de lista
    mountainBike = Modelo(choice, 
                    Stocks.stockBikes[choice][0], 
                    Stocks.stockBikes[choice][1], 
                    Stocks.stockBikes[choice][2], 
                    Stocks.stockBikes[choice][3], 
                    cliente, 
                    Stocks.stockBikes[choice][4])

    logging.info(mountainBike) 

    valor = mountainBike.valor

    metodoPago = input("Metodo de pago? efectivo/tarjeta").lower()

    recargo = cliente.calcularPrecio(metodoPago, valor)
    iva = cliente.calcularIva(21)
    cupon = cliente.aplicarCupon()

    logging.info(cliente.calcularPrecioFinal(recargo, iva, cupon))

if __name__ == '__main__':
    venta()
