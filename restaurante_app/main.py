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
    print("9. Salir")
    print("===============================")
    
    
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
            print("Ingrese un valor numerico valido.")
            
            
def guardar_productos(restaurante: Restaurante,archivo_servicio: ArchivoServicio) -> None:
    """
    Solicita al ArchivoServicio guardar los productos.
    """

    productos = restaurante.listar_producto()

    guardado = archivo_servicio.guardar_productos(
        productos
    )

    if guardado:
        print("Productos guardados correctamente.")
    else:
        print("No fue posible guardar los productos.")
            
            
def registrar_producto(restaurante: Restaurante, archivo_servicio:ArchivoServicio) -> None:
    """Solicita los datos y registra un producto."""
    
    print("\n--- REGISTRAR PRODUCTO ---")
    
    
    codigo = input("Ingrese el codigo: ").strip()
    nombre = input("Ingrese el nombre: ").strip()
    categoria = input("Ingrese la categoria: ").strip()
    precio = solicitar_precio()
    
    try:
        producto = Producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio
        )

        registrado = restaurante.registrar_producto(producto)

        if registrado:
            print("Producto registrado correctamente.")

            # Guardar después de registrar
            guardar_productos(restaurante, archivo_servicio)

        else:
            print("Error: ya existe un producto " "con ese código.")

    except ValueError as error:
        print(f"Error: {error}")

        
        
def buscar_producto(restaurante: Restaurante) -> None:
    """Busca un producto por codigo."""
    
    print("\n--- BUSCAR PRODUCTO ---")
    
    codigo = input("Ingrese el codigo del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)
    
    if producto is not None:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("No se encontro un producto con ese codigo.")
        
        
def actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Actualiza la información de un producto."""
    
    print("\n--- ACTUALIZAR PRODUCTO ---")
    
    codigo = input("Ingrese el codigo del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)
    
    if producto is None:
        print("No se encontro el producto.")
        return
    
    print("Producto actual: ")
    print(producto)
    
    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoria: ").strip()
    precio = solicitar_precio()
    
    try:
        actualizado = restaurante.actualizar_producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio
        )

        if actualizado:
            print("Producto actualizado correctamente.")

            # Guardar después de actualizar
            guardar_productos(restaurante, archivo_servicio)

        else:
            print("No fue posible actualizar el producto.")

    except ValueError as error:
        print(f"Error: {error}")

    
      
def eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    """Elimina un producto por codigo."""
    
    print("\n--- ELIMINAR PRODUCTO ---")
    
    codigo = input("Ingrese el codigo del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)
    
    if producto is None:
        print("No se encontro el producto.")
        return
    
    print("Producto encontrado:")
    print(producto)
    
    confirmación = input("¿Estas seguro de eliminarlo? (s/n):").strip().lower()
    
    if confirmación == "s":
        eliminado = restaurante.eliminar_producto(codigo)

        if eliminado:
            print("Producto eliminado correctamente.")

            # Guardar después de eliminar
            guardar_productos(restaurante, archivo_servicio)

        else:
            print("No fue posible eliminar el producto.")

    else:
        print("Operación cancelada.")


def listar_productos(restaurante: Restaurante) -> None:
    """Muestra todos los productos registrados."""
    
    print("\n--- LISTA DE PRODUCTOS ---")
    
    productos = restaurante.listar_producto()
    
    if not productos:
        print("No existe productos registrados.")
        return
    
    for producto in productos:
        print(producto)
        
        
def registrar_usuario(restaurante: Restaurante) -> None:
    """Solicita los datos y registrar un usuario."""
    
    print("\n---REGISTRAR USUARIO ---")
    
    identificación = input("Ingrese la identificación: ").strip()
    nombre = input("INgrese el nombre: ").strip()
    correo = input("Ingrese el correo: ").strip()
    
    try:
        usuario = Usuario(
            identificación=identificación,
            nombre=nombre,
            correo=correo
        )

        registrado = restaurante.registrar_usuario(usuario)

        if registrado:
            print("Usuario registrado correctamente.")
        else:
            print("Error: ya existe un usuario con esa identificación.")

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


def ejecutar_menu() -> None:
    """Ejecuta el menú principal del sistema."""

    restaurante = Restaurante()

    # Ubicación de productos.json
    ruta_json = (
        Path(__file__).resolve().parent
        / "datos"
        / "productos.json"
    )

    archivo_servicio = ArchivoServicio(str(ruta_json))

    # ==========================================
    # CARGAR PRODUCTOS AL INICIAR
    # ==========================================

    productos_cargados = (archivo_servicio.cargar_productos())

    restaurante.cargar_productos(productos_cargados)

    if productos_cargados:
        print(
            f"\nSe cargaron "
            f"{len(productos_cargados)} "
            f"producto(s) desde productos.json."
        )
    else:
        print("\nEl sistema inició sin productos almacenados.")

    # ==========================================
    # MENÚ
    # ==========================================

    while True:

        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_producto(restaurante,archivo_servicio)

            elif opcion == 2:
                buscar_producto(restaurante)

            elif opcion == 3:
                actualizar_producto(restaurante, archivo_servicio)

            elif opcion == 4:
                eliminar_producto(restaurante, archivo_servicio)

            elif opcion == 5:
                listar_productos(restaurante)

            elif opcion == 6:
                registrar_usuario(restaurante)

            elif opcion == 7:
                listar_usuarios(restaurante)

            elif opcion == 8:
                mostrar_categorias(restaurante)

            elif opcion == 9:
                print("\nGracias por utilizar el sistema de restaurante.")
                break

            else:
                print("Opción inválida. Seleccione del 1 al 9.")

        except ValueError:
            print("Error: debe ingresar un número válido.")


if __name__ == "__main__":
    ejecutar_menu()                           
                                
                