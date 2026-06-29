from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def main() -> None:
    servicio_restaurante = Restaurante("Agachaditos de don Xavi")

    producto1 = Producto("Guatita", 12.50, 30, True)
    producto2 = Producto("Papa reyena", 3.00, 10, True)
    producto3 = Producto("Encebollado", 9.75, 25, False)

    cliente1 = Cliente("Son Goku", "goku@ejemplo.com", 7, True)
    cliente2 = Cliente("Príncipe Vegeta", "vegeta@ejemplo.com", 2, False)
    cliente3 = Cliente("Trunks del Futuro", "trunks@ejemplo.com", 3, True)
    cliente4 = Cliente("Beerus dios de la destrucción", "beerus@ejemplo.com", 4, True)

    servicio_restaurante.agregar_producto(producto1)
    servicio_restaurante.agregar_producto(producto2)
    servicio_restaurante.agregar_producto(producto3)

    servicio_restaurante.agregar_cliente(cliente1)
    servicio_restaurante.agregar_cliente(cliente2)
    servicio_restaurante.agregar_cliente(cliente3)
    servicio_restaurante.agregar_cliente(cliente4)

    servicio_restaurante.mostrar_productos()
    servicio_restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()