from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    def __init__(
        self,
        productos: list[Producto] | None = None,
        usuarios: list[Usuario] | None = None,
        ventas: list[Venta] | None = None
    ):
        
        self._productos = productos or []
        self._usuarios = usuarios or []
        self._ventas = ventas or []
        
        self._indice_productos = {}
        self._indice_usuarios = {}
        
        
        self._ventas_por_usuario  = {}
        self._reconstruir_indices()
        
        
    def _reconstruir_indices(self) -> None:
        self._indice_productos.clear()
        self._indice_usuarios.clear()
        self._ventas_por_usuario.clear()

        for producto in self._productos:
            self._indice_productos[producto.codigo] = producto

        for usuario in self._usuarios:
            self._indice_usuarios[usuario.identificacion] = usuario

        for venta in self._ventas:
            if venta.usuario_id not in self._ventas_por_usuario:
                self._ventas_por_usuario[venta.usuario_id] = []

            self._ventas_por_usuario[venta.usuario_id].append(venta)
    
        
    def registrar_producto(self, producto: Producto ) -> bool:
        """Registrar un producto evitando codigos duplicados."""    
        
        
        if producto.codigo in self._indice_productos:
            return False

        self._productos.append(producto)
        self._indice_productos[producto.codigo] = producto

        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        # Búsqueda O(1) promedio mediante diccionario
        return self._indice_productos.get(codigo)
    
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
        
        
        producto.actualizar(
                nombre,
                categoria,
                precio,
                stock 
        )
        
        return True
    
    
    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto mediante su codigo."""
        
        producto = self.buscar_producto(codigo)
        
        if producto is None:
            return False
        
        self._productos.remove(producto)
        self._indice_productos[codigo]
        
        return True
    
    def listar_producto(self) -> list[Producto]:
        """Devuelve la lista de productos."""
        return self._productos
    

    
    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario evitando identificaciones duplicadas."""
        
        if usuario.identificación in self._indice_usuarios:
            return False
        
        self._usuarios.append(usuario)
        self._indice_usuarios[usuario.identificación] = usuario
        
        return True
    
    def buscar_usuario(self, identificación: str) -> Usuario | None:
        
        return self._indice_usuarios.get(identificación)    
    
    
    def listar_usuarios(self) -> list[Usuario]:
        """Devuelve la lista de usuarios."""
        
        return self._usuarios

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
        
        if usuario is None:
            return False
        
        if producto is None:
            return False

        # Comprobar cantidad
        if cantidad <= 0:
            return False

        # Comprobar stock
        if producto.stock < cantidad:
            return False

        # Crear la venta
        venta = Venta(
            usuario.identificación,
            producto.codigo,
            cantidad
        )

        # Agregar la venta a la colección
        self._ventas.append(venta)

        # Disminuir el stock
        producto.vender(cantidad)
        
        if usuario.identificación not in self._ventas_por_usuario:
            self._ventas_por_usuario[usuario.identificación] = []
            
        self._ventas_por_usuario[usuario.identificación].append(venta)    

        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        
        return self._ventas_por_usuario.get(identificacion_usuario, [])

    def listar_ventas(self) -> list[Venta]:

        return self._ventas


    # ==========================================
    # CATEGORÍAS
    # ==========================================

    def obtener_categorias(self) -> set[str]:

        return {
            producto.categoria
            for producto in self._productos
        }
