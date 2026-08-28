# Sistema de Restaurante - Semana 11

## Nombre del estudiante

**Jonnathan Paul Deleg Condo**

---

## 1. Descripción del sistema

El proyecto `restaurante_app` es un sistema de restaurante desarrollado en Python que permite administrar productos, usuarios y ventas mediante un menú interactivo por consola.

Esta versión corresponde a la evolución del proyecto desarrollado en semanas anteriores. Se incorporó el manejo de stock, la creación de la entidad `Venta` y la relación entre usuarios y productos mediante las ventas realizadas.

El sistema permite registrar, buscar, actualizar, eliminar y listar productos, registrar y consultar usuarios, realizar ventas y consultar las ventas realizadas por un usuario.

Además, la información se almacena en archivos JSON para que los productos, usuarios y ventas permanezcan disponibles después de cerrar y volver a ejecutar la aplicación.

---

## 2. Objetivo

El objetivo de esta actividad es ampliar el sistema de restaurante para trabajar con relaciones entre objetos y colecciones.

La operación principal incorporada es la venta de productos. Para realizar una venta, el sistema comprueba que exista el usuario, que exista el producto, que la cantidad sea válida y que exista suficiente stock.

Cuando la venta es correcta:

1. Se crea un objeto `Venta`.
2. La venta se agrega a la colección de ventas.
3. Se disminuye el stock del producto.
4. Se guardan los cambios en `productos.json`.
5. Se guarda la nueva venta en `ventas.json`.

---

## 3. Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md