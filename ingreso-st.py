import json

def cargar_datos():
    try:
        with open("estudiantes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def cargar_datos2():
    try:
        with open("clases.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open("estudiantes.json", "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)

def guardar_datos2(datos):
    with open("clases.json", "w", encoding="utf-8") as file:
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

def editar_clase(n_clase, nueva_informacion):
    clases = cargar_datos2()
    for clase in clases["clases"]:
        if clase["nb"] == n_clase:
            clase.update(nueva_informacion)
            guardar_datos2(clases)
            print(f"Información de la clase {n_clase} actualizada correctamente.")
            return
    else:
        print(f"Clase {n_clase} no encontrada.")

def modificar_clase():
    clases = cargar_datos2()  # Cargar datos de las clases
    print("Seleccione la clase que desea modificar:")
    for clase in clases["clases"]:
        print(f"Clase {clase['nb']}: Duración - {clase['duracion']}")
    clase_seleccionada = int(input("Ingrese el número de la clase que desea modificar: "))

    # Obtener información para modificar la clase
    nuevo_profesor = input("Ingrese el nombre del nuevo profesor: ")
    nuevo_aula = input("Ingrese el nombre de la nueva aula: ")
    nueva_ruta = input("Ingrese la nueva ruta de estudio: ")

    # Modificar la clase seleccionada
    for clase in clases["clases"]:
        if clase["nb"] == clase_seleccionada:
            clase["profesor"] = nuevo_profesor
            clase["aula"] = nuevo_aula
            clase["ruta"] = nueva_ruta
            break

    # Guardar los datos actualizados
    guardar_datos2(clases)
    print(f"Clase {clase_seleccionada} modificada exitosamente.")

def listar_estudiantes_inscritos():
    estudiantes = cargar_datos()
    inscritos = [estudiante for estudiante in estudiantes if estudiante["estado"] == "Inscrito"]

    if not inscritos:
        print("No hay estudiantes inscritos.")
        return

    print("Listado de estudiantes inscritos:")
    for estudiante in inscritos:
        print(f"ID: {estudiante['id']}, Nombre: {estudiante['nombres']}")

def agregar_notas_promedio(id_estudiante):
    estudiantes = cargar_datos()

    for estudiante in estudiantes:
        if estudiante["id"] == id_estudiante:
            nota_teoria = float(input("Ingrese la nota teórica: "))
            nota_practica = float(input("Ingrese la nota práctica: "))

            promedio = (nota_teoria + nota_practica) / 2
            print(f"El promedio es: {promedio}")

            if promedio >= 60:
                estudiante["estado"] = "Aprobado"
            else:
                estudiante["estado"] = "No aprobado"

            guardar_datos(estudiantes)
            print(f"Estado actualizado a: {estudiante['estado']}")
            break
    else:
        print(f"Estudiante con ID {id_estudiante} no encontrado.")

# Menú de opciones
estudiantes = cargar_datos()
guardar_datos(estudiantes)

while True:
    print("\n1. Agregar nuevo estudiante")
    print("2. Editar estudiante")
    print("3. Eliminar estudiante")
    print("4. Modificar clase")
    print("5. Agregar notas y actualizar estado")
    print("6. Salir")
    opcion = input("Seleccione una opción (1-7): ")

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
        modificar_clase()
    elif opcion == "5":
        listar_estudiantes_inscritos()
        id_estudiante = int(input("Ingrese el ID del estudiante al que desea agregar notas: "))
        agregar_notas_promedio(id_estudiante)
    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1-7).")
