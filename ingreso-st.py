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

def cargar_grupos():
    try:
        with open("grupos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_datos(datos):
    with open("estudiantes.json", "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)

def guardar_datos2(datos):
    with open("clases.json", "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=2, ensure_ascii=False)

def guardar_grupos(grupos):
    with open("grupos.json", "w", encoding="utf-8") as file:
        json.dump(grupos, file, indent=2, ensure_ascii=False)

def agregar_estudiante():
    nuevo_estudiante = {
        "Ti": input("Ingrese el número de TIentificación del estudiante: "),
        "nombres": input("Ingrese el nombre del estudiante: "),
        "apellidos": input("Ingrese los apellidos del estudiante: "),
        "direccion": input("Ingrese la dirección del estudiante: "),
        "acudiente": input("Ingrese el nombre del acudiente: "),
        "telefono_celular": input("Ingrese el teléfono celular del estudiante: "),
        "telefono_fijo": input("Ingrese el teléfono fijo del estudiante: "),
        "estado": input("Ingrese el estado del estudiante: "),
        "riesgo": input("Ingrese el riesgo del estudiante: "),
        "mo1":"",
        "mo2":"",
        "mo3":"",
        "mo4":"",
        "mo5":""
    }
    estudiantes = cargar_datos()
    estudiantes.append(nuevo_estudiante)
    guardar_datos(estudiantes)
    print(f"Nuevo estudiante agregado con TI {nuevo_estudiante['Ti']}.")

def editar_estudiante(Ti_estudiante, nueva_informacion):
    estudiantes = cargar_datos()
    for estudiante in estudiantes:
        if estudiante["Ti"] == Ti_estudiante:
            estudiante.update(nueva_informacion)
            guardar_datos(estudiantes)
            print(f"Información del estudiante con TI {Ti_estudiante} actualizada correctamente.")
            return
    else:
        print(f"Estudiante con TI {Ti_estudiante} no encontrado.")

def eliminar_estudiante(Ti_estudiante):
    estudiantes = cargar_datos()
    for estudiante in estudiantes[:]:
        if estudiante["Ti"] == Ti_estudiante:
            estudiantes.remove(estudiante)
            guardar_datos(estudiantes)
            print(f"Estudiante con TI {Ti_estudiante} eliminado correctamente.")
            return
    else:
        print(f"Estudiante con TI {Ti_estudiante} no encontrado.")

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

def agregar_ruta():
    nueva_ruta = input("Ingrese la nueva ruta de estudio: ")
    clases = cargar_datos2()
    rutas = clases.get("rutas", [])
    rutas.append(nueva_ruta)
    clases["rutas"] = rutas
    guardar_datos2(clases)
    print("Nueva ruta agregada exitosamente.")
    return

def modificar_clase():
    clases = cargar_datos2()
    print("Seleccione la clase que desea modificar:")
    for clase in clases["clases"]:
        print(f"Clase {clase['nb']}: Duración - {clase['duracion']}")
    clase_seleccionada = int(input("Ingrese el número de la clase que desea modificar: "))

    nuevo_profesor = input("Ingrese el nombre del nuevo profesor: ")
    nuevo_aula = input("Ingrese el nombre de la nueva aula: ")
    nueva_ruta = input("Ingrese la nueva ruta de estudio: ")

    for clase in clases["clases"]:
        if clase["nb"] == clase_seleccionada:
            clase["profesor"] = nuevo_profesor
            clase["aula"] = nuevo_aula
            clase["ruta"] = nueva_ruta
            break

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
        print(f"TI: {estudiante['Ti']}, Nombre: {estudiante['nombres']}")

def agregar_notas_promedio(Ti_estudiante):
    estudiantes = cargar_datos()

    for estudiante in estudiantes:
        if estudiante["Ti"] == Ti_estudiante:
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
        print(f"Estudiante con TI {Ti_estudiante} no encontrado.")

def agregar_estudiante_a_grupo():
    grupos = cargar_grupos()

    print("Grupos disponibles:")
    for grupo, info in grupos.items():
        print(f"{grupo}: Clase {info['clase']}")

    grupo_elegido = input("Seleccione el grupo al que desea agregar estudiantes: ")

    if grupo_elegido not in grupos:
        print("Grupo no válido.")
        return

    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que desea agregar: "))

    for _ in range(cantidad_estudiantes):
        nuevo_estudiante = {
            "Ti": input("Ingrese el número de identificación del estudiante: "),
            "nombres": input("Ingrese el nombre del estudiante: "),
            "apellidos": input("Ingrese los apellidos del estudiante: "),
            "direccion": input("Ingrese la dirección del estudiante: "),
            "acudiente": input("Ingrese el nombre del acudiente: "),
            "telefono_celular": input("Ingrese el teléfono celular del estudiante: "),
            "telefono_fijo": input("Ingrese el teléfono fijo del estudiante: "),
            "estado": input("Ingrese el estado del estudiante: "),
            "riesgo": input("Ingrese el riesgo del estudiante: ")
        }
        grupos[grupo_elegido]["Campers"].append(nuevo_estudiante)

    guardar_grupos(grupos)
    print(f"Estudiantes agregados al grupo {grupo_elegido} correctamente.")

def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Iniciar Sesión como Coordinador")
    print("2. Iniciar Sesión como Trainer")
    print("3. Iniciar Sesión como Camper")
    print("4. Salir del programa")

def menu_coordinador():
    print("\n--- Menú Coordinador ---")
    print("1. Agregar nuevo estudiante")
    print("2. Editar información de un estudiante")
    print("3. Eliminar estudiante")
    print("4. Modificar información de una clase")
    print("5. Agregar notas y actualizar estado del estudiante")
    print("6. Agregar nueva ruta de estudio")
    print("7. Listar estudiantes inscritos")
    print("8. Listar estudiantes aprobados")
    print("9. Listar estudiantes reprobados")
    print("10. Listar todas las clases")
    print("11. Listar todos los estudiantes")
    print("12. Agregar estudiantes a un grupo")
    print("13. Salir del programa")

def menu_trainer():
    print("\n--- Menú Trainer ---")
    print("1. Listar todas las clases")
    print("2. Salir del programa")

def menu_camper():
    print("\n--- Acceso denegado ---")
    print("Los campers no tienen acceso a este sistema.")

def iniciar_sesion_coordinador():
    while True:
        menu_coordinador()
        opcion = input("\nSeleccione una opción (1-13): ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            Ti_estudiante = input("Ingrese el TI del estudiante que desea editar: ")
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
            editar_estudiante(Ti_estudiante, nueva_informacion)
        elif opcion == "3":
            Ti_estudiante = input("Ingrese el TI del estudiante que desea eliminar: ")
            eliminar_estudiante(Ti_estudiante)
        elif opcion == "4":
            modificar_clase()
        elif opcion == "5":
            listar_estudiantes_inscritos()
            Ti_estudiante = input("Ingrese el TI del estudiante al que desea agregar notas: ")
            agregar_notas_promedio(Ti_estudiante)
        elif opcion == "6":
            agregar_ruta()
        elif opcion == "7":
            listar_estudiantes_inscritos()
        elif opcion == "8":
            # Código para listar estudiantes aprobados
            pass
        elif opcion == "9":
            # Código para listar estudiantes reprobados
            pass
        elif opcion == "10":
            # Código para listar todas las clases
            pass
        elif opcion == "11":
            # Código para listar todos los estudiantes
            pass
        elif opcion == "12":
            agregar_estudiante_a_grupo()
        elif opcion == "13":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1-13).")

def iniciar_sesion_trainer():
    while True:
        menu_trainer()
        opcion = input("\nSeleccione una opción (1-2): ")

        if opcion == "1":
            # Código para listar todas las clases
            pass
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1-2).")

def iniciar_sesion_camper():
    menu_camper()

while True:
    menu_principal()
    opcion = input("\nSeleccione una opción (1-4): ")

    if opcion == "1":
        iniciar_sesion_coordinador()
    elif opcion == "2":
        iniciar_sesion_trainer()
    elif opcion == "3":
        iniciar_sesion_camper()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1-4).")
