# SEMANA 5 

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python, aplicando de manera estricta los conceptos fundamentales de la **Programación Orientada a Objetos (POO)** y la organización modular de archivos de la Semana 5.

--------------------------------------------------------------------------------------------------------------

Para cumplir con la restricción de la actividad de **no reutilizar el ejemplo docente de la biblioteca**, se diseñó un entorno temático propio y original:

 **Identidad del Establecimiento:** El restaurante fue bautizado como **"Agachaditos de Don Xavi"** en honor al nombre del desarrollador (Mi persona), validando la autoría directa del proyecto.
 **Modelos para los Platillos:** Se configuró el menú utilizando gastronomía típica ecuatoriana, asignando precios (`float`), tiempos de preparación (`int`) y estados de disponibilidad (`bool`) del mundo real a platillos tradicionales como **Guatita**, **Papa Rellena** y **Encebollado**.

 **Modelos para los Clientes:** Se utilizaron nombres de personajes icónicos de la serie **Dragon Ball Z** (como *Son Goku*, *Príncipe Vegeta*, *Trunks del Futuro* y *Beerus*), asociándoles correos electrónicos simulados bajo un dominio estrictamente ficticio (`@ejemplo.com`).

--------------------------------------------------------------------------------------------------------------

El entorno de archivos está organizado bajo la arquitectura de paquetes requerida por la guía de estudio:

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
