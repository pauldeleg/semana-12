import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, carpeta_datos: str):
        self.carpeta_datos = Path(carpeta_datos)
        
        self.ruta_productos = (self.carpeta_datos / "productos.json")
        self.ruta_usuarios = (self.carpeta_datos / "usuarios.json")
        self.rutas_ventas = (self.carpeta_datos / "ventas.json")
        

    def guardar_productos(self, productos: list[Producto]) -> bool:
        """
        Guarda los productos en productos.json.
        """

        try:
            # Crear la carpeta datos si no existe
            self.carpeta_datos.mkdir(
                parents=True,
                exist_ok=True
            )

            # Convertir objetos Producto en diccionarios
            datos = [
                producto.to_dict()
                for producto in productos
            ]

            # Escribir el archivo utilizando UTF-8
            with open(
                self.ruta_productos,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:
            print("Error: no existen permisos para escribir productos.json.")
            return False

        except OSError as error:
            print(f"Error al guardar los productos: {error}")
            return False

    def cargar_productos(self) -> list[Producto]:
        """
        Carga los productos desde productos.json
        y reconstruye los objetos Producto.
        """

        try:
            # Leer el archivo utilizando UTF-8
            with open(
                self.ruta_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Error: productos.json tiene un formato inválido.")
            return []

        except PermissionError:
            print("Error: no existen permisos suficientes para leer productos.json.")
            return []

        except OSError as error:
            print(f"Error al leer productos.json: {error}")
            return []

        # Verificar que el JSON contenga una lista
        if not isinstance(datos, list):
            return []

        productos: list[Producto] = []

        # Reconstruir cada objeto Producto
        for registro in datos:

            try:
                productos.append(Producto.from_dict(registro))
                
            except (KeyError, ValueError, TypeError) as error:
                print(f"Producto invalido omitido: {error}")
        
        return productos
    
    def guardar_usuarios(self, usuarios: list[Usuario]) -> bool:
        
        try:
            self.carpeta_datos.mkdir(
                parents=True,
                exist_ok=True
            )
            
            datos = [
                usuario.to_dic()
                for usuario in usuarios    
                
            ]
            
            with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
                
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )
            return True
        
        except PermissionError:
            print("Error: no existe permisos para escribir usuarios.json")
            return False
        
        except OSError as error:
            print(f"Error al guardar usuarios: {error}")
            return False
        
    
    def cargar_usuarios(self) -> list[Usuario]:

        try:
            with open(
                self.ruta_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Error: usuarios.json tiene un formato inválido.")
            return []

        except PermissionError:
            print("Error: no existen permisos para leer usuarios.json.")
            return []

        except OSError as error:
            print(f"Error al leer usuarios.json: {error}")
            return []

        if not isinstance(datos, list):
            return []

        usuarios: list[Usuario] = []

        for registro in datos:
            try:
                usuarios.append(Usuario.from_dict(registro))

            except (KeyError, ValueError, TypeError) as error:
                print(f"Usuario inválido omitido: {error}")

        return usuarios

    # ==========================================
    # VENTAS
    # ==========================================

    def guardar_ventas(self, ventas: list[Venta]) -> bool:

        try:
            self.carpeta_datos.mkdir(
                parents=True,
                exist_ok=True
            )

            datos = [
                venta.to_dict()
                for venta in ventas
            ]

            with open(
                self.rutas_ventas,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except PermissionError:
            print("Error: no existen permisos para escribir ventas.json.")
            return False

        except OSError as error:
            print(f"Error al guardar ventas: {error}")
            return False

    def cargar_ventas(self) -> list[Venta]:

        try:
            with open(
                self.rutas_ventas,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("Error: ventas.json tiene un formato inválido.")
            return []

        except PermissionError:
            print("Error: no existen permisos para leer ventas.json.")
            return []

        except OSError as error:
            print(f"Error al leer ventas.json: {error}")
            return []

        if not isinstance(datos, list):
            return []

        ventas: list[Venta] = []

        for registro in datos:
            try:
                ventas.append(Venta.from_dict(registro))

            except (KeyError, ValueError, TypeError) as error:
                print(f"Venta inválida omitida: {error}")

        return ventas        
                
            
                

