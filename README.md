# POS System

Sistema de punto de venta desarrollado con FastAPI, MongoDB y JavaScript vanilla.

## Tecnologías

- Python 3.13
- FastAPI
- MongoDB
- Uvicorn
- HTML / CSS / JS

## Funcionalidades

- Gestión de productos (crear, listar, editar, eliminar)
- Control de stock automático al registrar ventas
- Registro de ventas con detalle de productos y total
- API REST documentada con Swagger UI

## Instalación

1. Clona el repositorio
2. Crea el entorno virtual: `python -m venv venv`
3. Actívalo: `venv\Scripts\activate`
4. Instala dependencias: `pip install -r requirements.txt`
5. Ejecuta el servidor: `uvicorn backend.main:app --reload`
6. Abre `http://127.0.0.1:8000/docs`

## Estado

En desarrollo — actualmente disponible el backend completo. Frontend en construcción.