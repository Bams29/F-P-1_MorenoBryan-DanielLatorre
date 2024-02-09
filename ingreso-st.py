import json
 
def cargar_datos():
    try:
        with open("estudiantes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open("estudiantes.json", "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)


def guardar_datos(datos):
    with open("estudiantes.json", "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)

def agregar_estudiante():
    nuevo_estudiante = {
        "nombres": input("Ingrese el nombre del estudiante: "),
        "apellidos": input("Ingrese los apellidos del estudiante: "),
        "direccion": input("Ingrese la dirección del estudiante: "),
        "acudiente": input("Ingrese el nombre del acudiente: "),
        "telefono_celular": input("Ingrese el teléfono celular del estudiante: "),
        "telefono_fijo": input("Ingrese el teléfono fijo del estudiante: "),
        "estado": input("Ingrese el estado del estudiante: "),
        "riesgo": input("Ingrese el riesgo del estudiante: ")
    }
    estudiantes = cargar_datos()
    if estudiantes:
        nuevo_estudiante["id"] = max(estudiantes, key=lambda x: x.get("id", 0)).get("id", 0) + 1
    else:
        nuevo_estudiante["id"] = 1
    estudiantes.append(nuevo_estudiante)
    guardar_datos(estudiantes)
    print(f"Nuevo estudiante agregado con ID {nuevo_estudiante['id']}.")

def editar_estudiante(id_estudiante, nueva_informacion):
    estudiantes = cargar_datos()
    for estudiante in estudiantes:
        if estudiante["id"] == id_estudiante:
            estudiante.update(nueva_informacion)
            guardar_datos(estudiantes)
            print(f"Información del estudiante con ID {id_estudiante} actualizada correctamente.")
            return
    else:
        print(f"Estudiante con ID {id_estudiante} no encontrado.")

def eliminar_estudiante(id):
    estudiantes = cargar_datos()
    for estudiante in estudiantes[:]:  # Crear una copia de la lista de estudiantes
        if estudiante["id"] == id:
            estudiantes.remove(estudiante)
            guardar_datos(estudiantes)
            print(f"Estudiante con ID {id} eliminado correctamente.")
            return
    else:
        print(f"Estudiante con ID {id} no encontrado.")
# Menú de opciones
estudiantes = cargar_datos()
guardar_datos(estudiantes)


while True:
    print("\n1. Agregar nuevo estudiante")
    print("2. Editar estudiante")
    print("3. Eliminar estudiante")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        id_estudiante = int(input("Ingrese el ID del estudiante que desea editar: "))
        nueva_informacion = {
            "nombres": input("Ingrese el nuevo nombre del estudiante: "),
            "apellidos": input("Ingrese los nuevos apellidos del estudiante: "),
            "direccion": input("Ingrese la nueva dirección del estudiante: "),
            "acudiente": input("Ingrese el nuevo nombre del acudiente: "),
            "telefono_celular": input("Ingrese el nuevo teléfono celular del estudiante: "),
            "telefono_fijo": input("Ingrese el nuevo teléfono fijo del estudiante: "),
            "estado": input("Ingrese el nuevo estado del estudiante: "),
            "riesgo": input("Ingrese el nuevo riesgo del estudiante: ")
        }
        editar_estudiante(id_estudiante, nueva_informacion)
    elif opcion == "3":
        id_estudiante = int(input("Ingrese el ID del estudiante que desea eliminar: "))
        eliminar_estudiante(id_estudiante)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1-4).")