class Venta:
    
    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ): 
        if not usuario_id.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")

        if not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.cantidad = cantidad

    def to_dict(self) -> dict:
        """
        Convierte la venta a un diccionario.
        """

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        """
        Reconstruye una Venta desde un diccionario.
        """

        return cls(
            usuario_id=str(datos["usuario_id"]),
            producto_codigo=str(datos["producto_codigo"]),
            cantidad=int(datos["cantidad"])
        )

    def __str__(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )