class Cliente:
    def __init__(self, nombre_completo: str, correo_electronico: str, numero_mesa: int, es_frecuente: bool):
        # Uso estricto de convenciones de nombres (snake_case) y anotaciones de tipo
        self.nombre_completo: str = nombre_completo
        self.correo_electronico: str = correo_electronico
        self.numero_mesa: int = numero_mesa
        self.es_frecuente: bool = es_frecuente

    def mostrar_informacion(self) -> str:
        return f"Cliente: {self.nombre_completo} | Contacto Ficticio: {self.correo_electronico}"

    def __str__(self) -> str:
        perfil_cliente = "Frecuente" if self.es_frecuente else "Regular"
        return f"{self.nombre_completo} (Mesa {self.numero_mesa} - {perfil_cliente})"