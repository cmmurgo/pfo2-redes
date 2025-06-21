import requests

API_URL = "http://127.0.0.1:5000"

session = requests.Session()

def menu():
    print("\n--- Menú Principal ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver página de tareas")
    print("4. Salir")

def registrar():
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    response = session.post(f"{API_URL}/registro", json={
        "usuario": usuario,
        "contraseña": contrasena
    })
    if response.status_code == 201:
        print("Usuario registrado con éxito.")
    else:
        print("Error al registrar:", response.json().get("error", "Desconocido"))

def login():
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    response = session.post(f"{API_URL}/login", json={
        "usuario": usuario,
        "contraseña": contrasena
    })
    if response.status_code == 200:
        print("Inicio de sesión exitoso.")
    else:
        print("Error de autenticación:", response.json().get("error", "Desconocido"))

def ver_tareas():
    response = session.get(f"{API_URL}/tareas")
    if response.status_code == 200 and "<html>" in response.text:
        print("Página de tareas:")
        print(response.text)
    else:
        print("No autenticado o error:", response.json().get("error", "Desconocido"))

def main():
    while True:
        menu()
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            registrar()
        elif opcion == "2":
            login()
        elif opcion == "3":
            ver_tareas()
        elif opcion == "4":
            print("Cerrando cliente.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
