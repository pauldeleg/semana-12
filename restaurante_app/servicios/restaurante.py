from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    def __init__(self):
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []
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
        precio: float,
        stock: int
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
                precio = precio,
                stock = stock
            )
        
            producto.nombre = producto_actualizado.nombre
            producto.categoria = producto_actualizado.categoria
            producto.precio = producto_actualizado.precio
            producto.stock = producto_actualizado.stock
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
    
    def cargar_productos(self,productos: list[Producto]) -> None:
        """
        Recibe los productos cargados desde JSON.
        """

        self.productos = productos.copy()

    
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""
        
        if self.buscar_usuario(usuario.identificación) is not None:
            return False
        
        self.usuarios.append(usuario)
        return True
    
    def buscar_usuario(self, identificación: str) -> Usuario | None:
        
        for usuario in self.usuarios:
            if usuario.identificación == identificación:
                return usuario
        return None    
    
    
    def listar_usuarios(self) -> list[Usuario]:
        """Devuelve la lista de usuarios."""
        
        return self.usuarios.copy()
    
    
    def cargar_usuarios(self,usuarios: list[Usuario]) -> None:

        self.usuarios = usuarios.copy()

    # ==========================================
    # VENTAS
    # ==========================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:
        """
        Registra una venta si el usuario y producto existen
        y existe stock suficiente.
        """

        usuario = self.buscar_usuario(identificacion_usuario)

        producto = self.buscar_producto(codigo_producto)
        
        if usuario is None or producto is None:
            return False

        # Comprobar cantidad
        if cantidad <= 0:
            return False

        # Comprobar stock
        if producto.stock < cantidad:
            return False

        # Crear la venta
        venta = Venta(
            usuario_id=usuario.identificación,
            producto_codigo=producto.codigo,
            cantidad=cantidad
        )

        # Agregar la venta a la colección
        self.ventas.append(venta)

        # Disminuir el stock
        producto.vender(cantidad)

        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        """
        Devuelve las ventas realizadas por un usuario.
        """

        ventas_usuario: list[Venta] = []

        for venta in self.ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:

        return self.ventas.copy()

    def cargar_ventas(self, ventas: list[Venta]) -> None:

        self.ventas = ventas.copy()

    # ==========================================
    # CATEGORÍAS
    # ==========================================

    def obtener_categorias(self) -> set[str]:

        return {
            producto.categoria
            for producto in self.productos
        }

    # ==========================================
    # INFORMACIÓN
    # ==========================================

    def obtener_informacion(self) -> tuple[str, str, str]:

        return self.informacion
