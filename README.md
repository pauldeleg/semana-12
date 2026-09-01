# Sistema de Restaurante - Semana 12

## Nombre del estudiante

**Jonnathan Paul Deleg Condo**

## 1. Descripción

El proyecto `restaurante_app` es un sistema de restaurante desarrollado en Python mediante Programación Orientada a Objetos.

La aplicación permite administrar productos, usuarios y ventas, además de controlar el stock disponible de los productos.

En la Semana 12 se realizó una mejora orientada al rendimiento mediante el uso de estructuras auxiliares de tipo `dict`. Se conservaron las listas principales para almacenar y recorrer los objetos, pero se incorporaron índices en memoria para realizar búsquedas frecuentes de forma más eficiente.

## 2. Objetivo de la Semana 12

El objetivo de esta semana fue optimizar las búsquedas y consultas del sistema utilizando colecciones adecuadas.

Se incorporaron índices auxiliares para:

- Buscar productos mediante su código.
- Buscar usuarios mediante su identificación.
- Consultar las ventas asociadas a un usuario.

Las listas principales no fueron eliminadas, ya que continúan siendo necesarias para almacenar, listar y persistir los objetos.

## 3. Estructura del proyecto
```text
restaurante_app/
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