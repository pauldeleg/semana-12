class Venta:
    
    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ): 
        if not usuario_id.strip():
            raise ValueError("La identificación del usuario es obligatoria.")

        if not producto_codigo.strip():
            raise ValueError("El código del producto es obligatorio.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad
        
    def convertir_a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Venta":
        return cls(
            usuario_id=datos["usuario_id"],
            producto_codigo=datos["producto_codigo"],
            cantidad=int(datos["cantidad"])
        )    
