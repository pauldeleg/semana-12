# restaurante_app - Semana 10

## Nombre completo del estudiante

**Jonnathan Paul Deleg Condo**

---

## Descripción del sistema

`restaurante_app` es un sistema desarrollado en Python para administrar
los productos y usuarios de un restaurante mediante programación
orientada a objetos.

El sistema permite registrar, buscar, actualizar, eliminar y listar
productos. También permite registrar y listar usuarios.

Como mejora correspondiente a la Semana 10, se incorporó la
persistencia de productos mediante un archivo en formato JSON. Esto
permite que los productos registrados no se pierdan cuando el programa
se cierra y puedan recuperarse automáticamente cuando la aplicación
vuelva a iniciarse.

La persistencia se aplica únicamente a los productos. Los usuarios
continúan almacenándose temporalmente en memoria.

---

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md