class Usuario:
    def __init__(
        self,
        identificación: str,
        nombre: str,
        correo: str
        
        ):
        
        if not identificación.strip():
            raise ValueError(
                "La identificación no puede estar vacía."
            )

        if not nombre.strip():
            raise ValueError(
                "El nombre no puede estar vacío."
            )

        if not correo.strip():
            raise ValueError(
                "El correo no puede estar vacío."
            )

        self.identificación = identificación.strip()
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        
    def __str__(self) -> str:
        return (
            f"Identificación: {self.identificación} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )    