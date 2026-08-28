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

        self.identificación = identificación.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        
    def to_dic(self) -> dict:
        return{
            "identificación": self.identificación,
            "nombre": self.nombre,
            "correo": self.correo
        }
        
    @classmethod
    def from_dict(cls, datos: dict) -> "Usuario":
        return cls(
            identificación = str(datos["identificación"]),
            nombre = str(datos["nombre"]),
            correo = str(datos["correo"])
        )       
        
    def __str__(self) -> str:
        return (
            f"Identificación: {self.identificación} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )    