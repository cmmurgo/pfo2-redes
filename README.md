# Sistema de Gestión de Tareas con API y Base de Datos

Este proyecto consiste en una API REST desarrollada con Flask para gestionar usuarios y tareas simples. 
Los datos se almacenan en SQLite y se accede a la API desde consola usando herramientas como `curl` o un cliente en Python.

---

## Requisitos
- Python 3.x
- `pip` (gestor de paquetes de Python)
- Flask
- SQLite3

## Instalación
git clone https://github.com/cmmurgo/pfo2-redes.git
cd gestion-tareas
pip install -r requirements.txt
python servidor.py

## Cómo probarlo con cliente.py
Este proyecto incluye un cliente simple en Python para probar la API desde consola.

# Pasos para probarlo:
# 1- Instalar la dependencia requests si no la tenés:

pip install requests

# 2- Ejecutar el cliente:

python cliente.py

# 3- Ingresar usuario y contraseña cuando se solicite:

Si el usuario no existe, el cliente intentará registrarlo automáticamente.
Luego, se realizará el login y se consultará el endpoint /tareas.

# 4- Verás en consola las respuestas de cada paso:
Usuario registrado con éxito.
Inicio de sesión exitoso.
Resultado del login.
Página HTML de bienvenida

