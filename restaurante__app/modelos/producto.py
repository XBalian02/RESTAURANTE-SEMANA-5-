class Producto:
    def __init__(self, nombre: str, precio: float, tiempo_preparacion_minutos: int, disponible: bool):
        self.nombre: str = nombre
        self.precio: float = precio
        
        self.tiempo_preparacion_minutos: int = tiempo_preparacion_minutos
        self.disponible: bool = disponible

    def mostrar_informacion(self) -> str:
        estado_platillo = "Disponible" if self.disponible else "No Disponible"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Estado: {estado_platillo}"

    def __str__(self) -> str:
        return f"{self.nombre} (${self.precio:.2f})"