from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_sucursal: str):
        self.nombre_sucursal: str = nombre_sucursal
        
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def mostrar_productos(self) -> None:
        print(f"\n--- MENÚ DE PRODUCTOS: {self.nombre_sucursal.upper()} ---")
        for producto in self.lista_productos:
            print(producto.mostrar_informacion())

    def mostrar_clientes(self) -> None:
        print("\n--- CLIENTES REGISTRADOS EN SALA ---")
        for cliente in self.lista_clientes:
            print(cliente)