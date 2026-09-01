import json

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, carpeta: str = "datos"):
        self.carpeta = carpeta 
        
    def _ruta(self, nombre_archivo: str) -> str:
        return f"{self.carpeta}/{nombre_archivo}"
    

    def cargar_productos(self) -> list[Producto]:
        ruta = self._ruta("productos.json")

        try:
            # Leer el archivo utilizando UTF-8
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                
            productos: list[Producto] = []
            
            for registro in datos:
                try:
                    producto = Producto.desde_diccionario(registro)
                    productos.append(producto)
                except (KeyError, ValueError, TypeError) as error:
                    print(f"Producto opmitido: {error}")
            return productos
                        

        except FileNotFoundError:
            print("productos.json no existe. Se iniciara con productos vacios.")
            return []

        except json.JSONDecodeError:
            print("productos.json contiene JSON inválido.")
            return []

        except PermissionError:
            print("No existen permisos para leer productos.json.")
            return []

    def guardar_productos(self, productos: list[Producto]) -> bool:
        ruta = self._ruta("productos.json")

        try:
            datos = [producto.convertir_a_diccionario() 
                     for producto in productos
            ]

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False,)

            return True

        except PermissionError:
            print("No existen permisos para escribir productos.json.")
            return False
        
    def cargar_usuarios(self) -> list[Usuario]:
        ruta = self._ruta("usuarios.json")

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            usuarios: list[Usuario] = []

            for registro in datos:
                try:
                    usuario = Usuario.desde_diccionario(registro)
                    usuarios.append(usuario)
                except (KeyError, ValueError, TypeError) as error:
                    print(f"Usuario omitido: {error}")

            return usuarios

        except FileNotFoundError:
            print("usuarios.json no existe. Se iniciará con usuarios vacíos.")
            return []

        except json.JSONDecodeError:
            print("usuarios.json contiene JSON inválido.")
            return []

        except PermissionError:
            print("No existen permisos para leer usuarios.json.")
            return []
            

    def guardar_usuarios(self, usuarios: list[Usuario]) -> bool:
        ruta = self._ruta("usuarios.json")
        
        try:
            datos = [
                usuario.convertir_a_diccionario()
                for usuario in usuarios
            ]

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

            return True

        except PermissionError:
            print("No existen permisos para escribir usuarios.json.")
            return False
        
    
    def cargar_ventas(self) -> list[Venta]:
        ruta = self._ruta("ventas.json")

        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            ventas: list[Venta] = []

            for registro in datos:
                try:
                    venta = Venta.desde_diccionario(registro)
                    ventas.append(venta)
                except (KeyError, ValueError, TypeError) as error:
                    print(f"Venta omitida: {error}")

            return ventas

        except FileNotFoundError:
            print("ventas.json no existe. Se iniciará con ventas vacías.")
            return []

        except json.JSONDecodeError:
            print("ventas.json contiene JSON inválido.")
            return []

        except PermissionError:
            print("No existen permisos para leer ventas.json.")
            return []

    def guardar_ventas(self, ventas: list[Venta]) -> bool:
        ruta = self._ruta("ventas.json")

        try:
            datos = [
                venta.convertir_a_diccionario()
                for venta in ventas
            ]

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)

            return True

        except PermissionError:
            print("No existen permisos para escribir ventas.json.")
            return False

