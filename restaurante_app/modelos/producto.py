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
            raise ValueError("El stock no puede ser negaivo.")
        

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self. precio = precio
        self.stock = stock
        
    def vender(self, cantidad: int ) -> None:
        
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        
        if cantidad > self.stock:
            raise ValueError("No existe stock suficiente.")
        
        self.stock -= cantidad
           
        
    def to_dict(self) -> dict:
        """
        Convierte el objeto Producto en un diccionario
        para poder almacenarlo en formato JSON.
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock" : self.stock
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        """
        Reconstruye un objeto Producto a partir
        de un diccionario obtenido desde JSON.
        """
        return cls(
            codigo=str(datos["codigo"]),
            nombre=str(datos["nombre"]),
            categoria=str(datos["categoria"]),
            precio=float(datos["precio"]),
            stock=int(datos["stock"])
        )    
        
    def __str__(self) -> str:
        return (
            f"Codigo: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoria: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
            f"Stock: {self.stock}"
        )    
        