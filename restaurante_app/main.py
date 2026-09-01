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
    
    
def main() -> None:

    archivo = ArchivoServicio()

    productos = archivo.cargar_productos()
    usuarios = archivo.cargar_usuarios()
    ventas = archivo.cargar_ventas()

    restaurante = Restaurante(productos, usuarios, ventas)

    print("\nDatos cargados correctamente.")
    print(f"Productos: {len(productos)}")
    print(f"Usuarios: {len(usuarios)}")
    print(f"Ventas: {len(ventas)}")

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        # ============================================
        # REGISTRAR PRODUCTO
        # ============================================

        if opcion == "1":

            try:
                codigo = input("Código: ").strip()
                nombre = input("Nombre: ").strip()
                categoria = input("Categoría: ").strip()
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))

                producto = Producto(
                    codigo,
                    nombre,
                    categoria,
                    precio,
                    stock
                )

                if restaurante.registrar_producto(producto):
                    archivo.guardar_productos(restaurante.listar_producto())
                    print("Producto registrado correctamente.")
                else:
                    print("Ya existe un producto con ese código.")

            except ValueError as error:
                print(f"Error: {error}")

        # ============================================
        # BUSCAR PRODUCTO
        # ============================================

        elif opcion == "2":

            codigo = input("Ingrese el código del producto: ").strip()

            producto = restaurante.buscar_producto(codigo)

            if producto:
                print("\nProducto encontrado:")
                print(f"Código: {producto.codigo}")
                print(f"Nombre: {producto.nombre}")
                print(f"Categoría: {producto.categoria}")
                print(f"Precio: ${producto.precio:.2f}")
                print(f"Stock: {producto.stock}")
            else:
                print("Producto no encontrado.")

        # ============================================
        # ACTUALIZAR PRODUCTO
        # ============================================

        elif opcion == "3":

            try:
                codigo = input("Código del producto: ").strip()

                producto = restaurante.buscar_producto(codigo)

                if producto is None:
                    print("Producto no encontrado.")
                    continue

                nombre = input("Nuevo nombre: ").strip()
                categoria = input("Nueva categoría: ").strip()
                precio = float(input("Nuevo precio: "))
                stock = int(input("Nuevo stock: "))

                if restaurante.actualizar_producto(
                    codigo,
                    nombre,
                    categoria,
                    precio,
                    stock
                ):
                    archivo.guardar_productos(restaurante.listar_producto())
                    print("Producto actualizado correctamente.")

            except ValueError as error:
                print(f"Error: {error}")

        # ============================================
        # ELIMINAR PRODUCTO
        # ============================================

        elif opcion == "4":

            codigo = input("Código del producto: ").strip()

            if restaurante.eliminar_producto(codigo):
                archivo.guardar_productos(restaurante.listar_productos())
                print("Producto eliminado correctamente.")
            else:
                print("Producto no encontrado.")

        # ============================================
        # LISTAR PRODUCTOS
        # ============================================

        elif opcion == "5":

            productos = restaurante.listar_producto()

            if not productos:
                print("No existen productos registrados.")
            else:
                print("\nPRODUCTOS")

                for producto in productos:
                    print(
                        f"{producto.codigo} | "
                        f"{producto.nombre} | "
                        f"{producto.categoria} | "
                        f"${producto.precio:.2f} | "
                        f"Stock: {producto.stock}"
                    )

        # ============================================
        # REGISTRAR USUARIO
        # ============================================

        elif opcion == "6":

            try:
                identificación = input("Identificación: ").strip()
                nombre = input("Nombre: ").strip()
                correo = input("Correo: ").strip()

                usuario = Usuario(identificación, nombre, correo)

                if restaurante.registrar_usuario(usuario):
                    archivo.guardar_usuarios(restaurante.listar_usuarios())
                    print("Usuario registrado correctamente.")
                else:
                    print("Ya existe un usuario con esa identificación.")

            except ValueError as error:
                print(f"Error: {error}")

        # ============================================
        # BUSCAR USUARIO
        # ============================================

        elif opcion == "7":

            identificacion = input("Ingrese la identificación: ").strip()

            usuario = restaurante.buscar_usuario(identificacion)

            if usuario:
                print("\nUsuario encontrado:")
                print(f"Identificación: {usuario.identificacion}")
                print(f"Nombre: {usuario.nombre}")
                print(f"Correo: {usuario.correo}")
            else:
                print("Usuario no encontrado.")

        # ============================================
        # LISTAR USUARIOS
        # ============================================

        elif opcion == "8":

            usuarios = restaurante.listar_usuarios()

            if not usuarios:
                print("No existen usuarios registrados.")
            else:
                print("\nUSUARIOS")

                for usuario in usuarios:
                    print(
                        f"{usuario.identificacion} | "
                        f"{usuario.nombre} | "
                        f"{usuario.correo}"
                    )

        # ============================================
        # VENDER PRODUCTO
        # ============================================

        elif opcion == "9":

            try:
                identificacion = input("Identificación del usuario: ").strip()

                codigo = input("Código del producto: ").strip()

                cantidad = int(input("Cantidad: "))

                producto = restaurante.buscar_producto(codigo)

                if producto is None:
                    print("El producto no existe.")
                    continue

                if restaurante.buscar_usuario(identificacion) is None:
                    print("El usuario no existe.")
                    continue

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    continue

                if cantidad > producto.stock:
                    print(
                        f"Stock insuficiente. "
                        f"Disponible: {producto.stock}"
                    )
                    continue

                if restaurante.vender_producto(
                    codigo,
                    identificacion,
                    cantidad
                ):

                    archivo.guardar_productos(restaurante.listar_productos())

                    archivo.guardar_ventas(restaurante.listar_ventas())

                    print("Venta realizada correctamente.")
                    print(f"Stock restante: {producto.stock}")

            except ValueError as error:
                print(f"Error: {error}")

        # ============================================
        # CONSULTAR VENTAS DE USUARIO
        # ============================================

        elif opcion == "10":

            identificacion = input("Identificación del usuario: ").strip()

            usuario = restaurante.buscar_usuario(identificacion)

            if usuario is None:
                print("El usuario no existe.")
                continue

            ventas = restaurante.consultar_ventas_usuario(identificacion)

            if not ventas:
                print("El usuario no tiene ventas.")
            else:
                print(f"\nVentas de {usuario.nombre}:")

                for venta in ventas:

                    producto = restaurante.buscar_producto(venta.producto_codigo)

                    nombre_producto = (
                        producto.nombre
                        if producto
                        else "Producto no disponible"
                    )

                    print(
                        f"Producto: {nombre_producto} | "
                        f"Código: {venta.producto_codigo} | "
                        f"Cantidad: {venta.cantidad}"
                    )

        # ============================================
        # LISTAR VENTAS
        # ============================================

        elif opcion == "11":

            ventas = restaurante.listar_ventas()

            if not ventas:
                print("No existen ventas registradas.")
            else:
                print("\nVENTAS")

                for venta in ventas:

                    usuario = restaurante.buscar_usuario(venta.usuario_id)

                    producto = restaurante.buscar_producto(venta.producto_codigo)

                    nombre_usuario = (
                        usuario.nombre
                        if usuario
                        else "Usuario no disponible"
                    )

                    nombre_producto = (
                        producto.nombre
                        if producto
                        else "Producto no disponible"
                    )

                    print(
                        f"Usuario: {nombre_usuario} | "
                        f"Producto: {nombre_producto} | "
                        f"Cantidad: {venta.cantidad}"
                    )

        # ============================================
        # CATEGORÍAS
        # ============================================

        elif opcion == "12":

            categorias = restaurante.obtener_categorias()

            if categorias:
                print("\nCATEGORÍAS:")
                for categoria in sorted(categorias):
                    print(f"- {categoria}")
            else:
                print("No existen categorías.")

        # ============================================
        # SALIR
        # ============================================

        elif opcion == "13":

            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()