from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante



def mostrar_menu() -> None:
    """Muestra el menu principal."""
    
    print("\n==============================")
    print("    SISTEMA DE RESTAURANTE     ")
    print("================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")  
    print("5. Listar productos")
    print("--------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("-------------------------------")
    print("8. Mostrar categorias")
    print("9. Vender producto")
    print("10. Consultar ventas de usuario")
    print("11. Listar ventas")
    print("12. Salir")
    print("===============================")
    
    
def solicitar_entero(mensaje: str ) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un numero entero.")    
    
    
def solicitar_precio() -> float:
    """Solicita y valida el precio de un producto."""
    
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            return precio
        
        except ValueError:
            print("Ingrese un precio valido.")
            
            
def guardar_productos(restaurante: Restaurante,archivo_servicio: ArchivoServicio) -> None:
    """
    Solicita al ArchivoServicio guardar los productos.
        """
    if archivo_servicio.guardar_productos(restaurante.listar_producto()):
        
        print("Productos guardados correctamente.")
        
        
def guardar_usuarios(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:

    if archivo_servicio.guardar_usuarios(restaurante.listar_usuarios()):
        print("Usuarios guardados correctamente.")


def guardar_ventas(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:

    if archivo_servicio.guardar_ventas(restaurante.listar_ventas()):
        print("Ventas guardadas correctamente.")
        
        
def registrar_producto(restaurante: Restaurante, archivo_servicio:ArchivoServicio) -> None:
    """Solicita los datos y registra un producto."""
    
    print("\n--- REGISTRAR PRODUCTO ---")
    
    
    codigo = input("Codigo: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoria: ").strip()
    precio = solicitar_precio()
    stock = solicitar_entero("Stock inicial: ")
    
    
    try:
        producto = Producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock
        )

        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")

            # Guardar después de registrar
            guardar_productos(restaurante, archivo_servicio)

        else:
            print("Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"Error: {error}")

        
        
def buscar_producto(restaurante: Restaurante) -> None:
    """Busca un producto por codigo."""
    
    print("\n--- BUSCAR PRODUCTO ---")
    
    codigo = input("Codigo del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)
    
    if producto is not None:
        print(producto)
    else:
        print("Producto no encontrado.")
        
        
def actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Actualiza la información de un producto."""
    
    print("\n--- ACTUALIZAR PRODUCTO ---")
    
    codigo = input("Codigo del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)
    
    if producto is None:
        print("Producto no encontrado.")
        return
    
    print("Producto actual: ")
    print(producto)
    
    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoria: ").strip()
    precio = solicitar_precio()
    
    stock = solicitar_entero("Nuevo stock: ")
    
    try:
        if restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        ):
             
            print("Producto actualizado correctamente.")

            # Guardar después de actualizar
            guardar_productos(restaurante, archivo_servicio)

        else:
            print("No fue posible actualizar.")

    except ValueError as error:
        print(f"Error: {error}")

    
      
def eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Elimina un producto por codigo."""
    
    print("\n--- ELIMINAR PRODUCTO ---")
    
    codigo = input("Codigo del producto: ").strip()
    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
        
        guardar_productos(restaurante, archivo_servicio)
        
    else:
        print("Producto no encontrado.")  


def listar_productos(restaurante: Restaurante) -> None:
    """Muestra todos los productos registrados."""
    
    print("\n--- LISTA DE PRODUCTOS ---")
    
    productos = restaurante.listar_producto()
    
    if not productos:
        print("No existe productos.")
        return
    
    for producto in productos:
        print(producto)
        
        
def registrar_usuario(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Solicita los datos y registrar un usuario."""
    
    print("\n---REGISTRAR USUARIO ---")
    
    identificación = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    
    try:
        usuario = Usuario(
            identificación,
            nombre,
            correo
        )

        if restaurante.registrar_usuario(usuario):
            
            print("Usuario registrado correctamente.")
            
            guardar_usuarios(
                restaurante,
                archivo_servicio
            )
            
        else:
            print("Ya existe un usuario con esa identificación.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    """Muestra todos los usuarios registrados."""

    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias(restaurante: Restaurante) -> None:
    """Muestra las categorías únicas."""

    print("\n--- CATEGORÍAS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")
        
        
def vender_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:

    print("\n--- VENDER PRODUCTO ---")

    identificacion = input("Identificación del usuario: ").strip()

    codigo = input("Código del producto: ").strip()

    cantidad = solicitar_entero("Cantidad a comprar: ")

    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("Error: el usuario no existe.")
        return

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Error: el producto no existe.")
        return

    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor que cero.")
        return

    if producto.stock < cantidad:
        print(
            f"Stock insuficiente. "
            f"Stock disponible: {producto.stock}"
        )
        return

    if restaurante.vender_producto(
        codigo,
        identificacion,
        cantidad
    ):

        print("Venta registrada correctamente.")

        guardar_productos(restaurante, archivo_servicio)

        guardar_ventas(restaurante, archivo_servicio)

    else:
        print("No fue posible realizar la venta.")


def consultar_ventas_usuario(restaurante: Restaurante) -> None:

    print("\n--- VENTAS DE UN USUARIO ---")

    identificacion = input("Identificación del usuario: ").strip()

    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("El usuario no existe.")
        return

    ventas = restaurante.consultar_ventas_usuario(identificacion)

    if not ventas:
        print("El usuario no tiene ventas registradas.")
        return

    for venta in ventas:

        producto = restaurante.buscar_producto(venta.producto_codigo)

        if producto is not None:
            print(
                f"Producto: {producto.nombre} | "
                f"Código: {producto.codigo} | "
                f"Cantidad: {venta.cantidad}"
            )
        else:
            print(venta)


def listar_ventas(restaurante: Restaurante) -> None:

    print("\n--- TODAS LAS VENTAS ---")

    ventas = restaurante.listar_ventas()

    if not ventas:
        print("No existen ventas registradas.")
        return

    for venta in ventas:

        producto = restaurante.buscar_producto(venta.producto_codigo)

        usuario = restaurante.buscar_usuario(venta.usuario_id)

        nombre_producto = (
            producto.nombre
            if producto is not None
            else "Producto no disponible"
        )

        nombre_usuario = (
            usuario.nombre
            if usuario is not None
            else "Usuario no disponible"
        )

        print(
            f"Usuario: {nombre_usuario} | "
            f"Producto: {nombre_producto} | "
            f"Cantidad: {venta.cantidad}"
        )
        
        
def ejecutar_menu() -> None:
    """Ejecuta el menú principal del sistema."""

    restaurante = Restaurante()

    # Ubicación de productos.json
    ruta_datos = (Path(__file__).resolve().parent / "datos")

    archivo_servicio = ArchivoServicio(str(ruta_datos))

    # ==========================================
    # CARGAR LAS TRES COLECCIONES
    # ==========================================
    
    productos = archivo_servicio.cargar_productos()
    usuarios = archivo_servicio.cargar_usuarios()
    ventas = archivo_servicio.cargar_ventas()
    
    restaurante.cargar_productos(productos)
    restaurante.cargar_usuarios(usuarios)
    restaurante.cargar_ventas(ventas)

    print("\n========================================")
    print("     DATOS CARGADOS CORRECTAMENTE")
    print("========================================")
    print(f"Productos: {len(productos)}")
    print(f"Usuarios: {len(usuarios)}")
    print(f"Ventas: {len(ventas)}")

    while True:

        mostrar_menu()

        opcion = solicitar_entero(
            "Seleccione una opción: "
        )

        if opcion == 1:

            registrar_producto(restaurante, archivo_servicio)

        elif opcion == 2:

            buscar_producto(
                restaurante
            )

        elif opcion == 3:

            actualizar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == 4:

            eliminar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == 5:

            listar_productos(
                restaurante
            )

        elif opcion == 6:

            registrar_usuario(
                restaurante,
                archivo_servicio
            )

        elif opcion == 7:

            listar_usuarios(
                restaurante
            )

        elif opcion == 8:

            mostrar_categorias(
                restaurante
            )

        elif opcion == 9:

            vender_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == 10:

            consultar_ventas_usuario(
                restaurante
            )

        elif opcion == 11:

            listar_ventas(
                restaurante
            )

        elif opcion == 12:

            print(
                "\nGracias por utilizar "
                "el sistema de restaurante."
            )
            break

        else:

            print(
                "Opción inválida."
            )


if __name__ == "__main__":
    ejecutar_menu()
    