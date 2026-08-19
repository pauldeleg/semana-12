from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.información: tuple[str, str, str] = (
            "Restaurante Las Delicias",
            "Av. Ordonez Lasso ",
            "09987653721"
        )
        
    def registrar_producto(self, producto: Producto ) -> bool:
        """Registrar un producto evitando codigos duplicados."""    
        
        
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self.productos.append(producto)
        return True
    
    def buscar_producto(self, codigo: str) -> Producto | None:
        """Busca un producto utilizando su codigo."""
        
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
            
        return None
    
    def actualizar_producto(
        self, 
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    )   -> bool:
        
        """Actualiza los datos de un producto existente."""
        
        producto = self.buscar_producto(codigo)
        
        if producto is None:
            return False
        
        try:
            producto_actualizado = Producto(
                codigo = codigo,
                nombre = nombre,
                categoria = categoria,
                precio = precio
            )
        
            producto.nombre = producto_actualizado.nombre
            producto.categoria = producto_actualizado.categoria
            producto.precio = producto_actualizado.precio
        
            return True
        except ValueError:
             return False
    
    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto mediante su codigo."""
        
        producto = self.buscar_producto(codigo)
        
        if producto is None:
            return False
        
        self.productos.remove(producto)
        return True
    
    def listar_producto(self) -> list[Producto]:
        """Devuelve la lista de productos."""
        return self.productos.copy()
    
    def cargar_productos(
        self,
        productos: list[Producto]
    ) -> None:
        """
        Recibe los productos cargados desde JSON.
        """

        self.productos = productos.copy()

    
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""
        
        for usuario_registrado in self.usuarios:
            if (usuario_registrado.identificación == usuario.identificación):
                return False
            
        self.usuarios.append(usuario)
        return True
    
    
    def listar_usuarios(self) -> list[Usuario]:
        """Devuelve la lista de usuarios."""
        
        return self.usuarios.copy()
    
    
    def obtener_categorias(self) -> set[str]:
        """Obtiene las categorias unicas de los productos."""
        
        return {
            producto.categoria
            for producto in self.productos
            
        }    
        
        
    def ontener_información(self) -> tuple[str, str, str]:
        """Devuelve la información estable del restaurante."""
        
        return self.información    