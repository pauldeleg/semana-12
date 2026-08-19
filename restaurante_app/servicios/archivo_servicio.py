import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:
    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = Path(ruta_archivo)

    def guardar_productos(self, productos: list[Producto]) -> bool:
        """
        Guarda los productos en productos.json.
        """

        try:
            # Crear la carpeta datos si no existe
            self.ruta_archivo.parent.mkdir(
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
                self.ruta_archivo,
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
            print("Error: no existen permisos suficientes para escribir el archivo.")
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
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            print("No existe productos.json. El sistema iniciará con una colección vacía.")
            return []

        except json.JSONDecodeError:
            print("Error: productos.json no contiene un formato JSON válido.")
            return []

        except PermissionError:
            print("Error: no existen permisos suficientes para leer productos.json.")
            return []

        except OSError as error:
            print(f"Error al leer productos.json: {error}")
            return []

        # Verificar que el JSON contenga una lista
        if not isinstance(datos, list):
            print("Error: el archivo JSON debe contener una lista de productos.")
            return []

        productos: list[Producto] = []

        # Reconstruir cada objeto Producto
        for registro in datos:

            try:
                if not isinstance(registro, dict):
                    raise ValueError("El registro no tiene formato de diccionario.")

                producto = Producto.from_dict(registro)
                productos.append(producto)

            except KeyError as error:
                print(
                    "Se omitió un registro porque falta "
                    f"la clave {error}."
                )

            except ValueError as error:
                print(f"Se omitió un registro inválido: {error}")

            except (TypeError, OverflowError) as error:
                print(
                    f"Se omitió un registro por datos incorrectos: "
                    f"{error}"
                )

        return productos