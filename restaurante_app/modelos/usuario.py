class Usuario:
    def __init__(
        self,
        identificación: str,
        nombre: str,
        correo: str
        
    ):
        
        if not identificación.strip():
            raise ValueError("La identificación no puede estar vacía.")

        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not correo.strip():
            raise ValueError("El correo no puede estar vacío.")

        self.identificación = identificación
        self.nombre = nombre
        self.correo = correo
        
        
    def convertir_a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            correo=datos["correo"]
        )