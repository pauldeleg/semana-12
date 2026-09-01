class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int = 0
        
    ): 
        
        if not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self. precio = precio
        self.stock = stock
        
    def vender(self, cantidad: int ) -> None:
        
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")
        
        self.stock -= cantidad
           
        
    def actualizar(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> None:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Producto":
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=float(datos["precio"]),
            stock=int(datos["stock"])
        )