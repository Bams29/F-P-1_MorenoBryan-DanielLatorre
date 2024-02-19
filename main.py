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
        "Ti": input("Ingrese el número de Identificación del estudiante: "),
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

def listar_clases():
    clases = cargar_datos2()
    profesores = clases["profesores"]

    print("Listado de clases:")
    for clase in clases["clases"]:
        print(f"Clase {clase['nb']}:")
        print(f"  Duración: {clase['duracion']}")
        if clase['profesor'] != 'sin especificar':
            profesor = next((p['nombre'] for p in profesores if p['nombre'] == clase['profesor']), 'Desconocido')
            print(f"  Profesor: {profesor}")
        else:
            print("  Profesor: sin especificar")
        print(f"  Aula/s: {clase['aula/s']}")
        print()

def listar_estudiantes_inscritos():
    estudiantes = cargar_datos()
    inscritos = [estudiante for estudiante in estudiantes if estudiante["estado"] == "Inscrito" or estudiante["estado"] == "inscrito"]

    if not inscritos:
        print("No hay estudiantes inscritos.")
        return

    print("Listado de estudiantes inscritos:")
    for estudiante in inscritos:
        print(f"TI: {estudiante['Ti']}, Nombre: {estudiante['nombres']}")

def listar_estudiantes_aprobados():
    estudiantes = cargar_datos()
    aprobados = [estudiante for estudiante in estudiantes if estudiante["estado"] == "Aprobado" or estudiante["estado"] == "aprobado"]

    if not aprobados:
        print("No hay estudiantes Aprobados.")
        return

    print("Listado de estudiantes Aprobados:")
    for estudiante in aprobados:
        print(f"TI: {estudiante['Ti']}, Nombre: {estudiante['nombres']}")

def listar_estudiantes_reprobados():
    estudiantes = cargar_datos()
    reprobados = [estudiante for estudiante in estudiantes if estudiante["estado"] == "No Aprobado" or estudiante["estado"] == "No aprobado"]

    if not reprobados:
        print("No hay estudiantes reprobados.")
        return

    print("Listado de estudiantes reprobados:")
    for estudiante in reprobados:
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

def matricular_estudiantes():
    estudiantes = cargar_datos()

    aprobados = [estudiante for estudiante in estudiantes if estudiante["estado"].lower() == "aprobado"]

    if not aprobados:
        print("No hay estudiantes aprobados para matricular.")
        return

    print("Estudiantes Aprobados:")
    for i, estudiante in enumerate(aprobados, start=1):
        print(f"{i}. TI: {estudiante['Ti']}, Nombre: {estudiante['nombres']}")

    while True:
        opcion = input("Ingrese el numero del estudiante que desea matricular.")

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(aprobados):
                estudiante_elegido = aprobados[opcion - 1]
                break
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    grupos = cargar_grupos()

    
    print("Grupos disponibles:")
    for grupo, info in grupos.items():
        print(f"{grupo}: Clase {info['clase'][0]}")

    
    grupo_elegido = input("Seleccione el grupo al que desea matricular al estudiante: ")

    if grupo_elegido not in grupos:
        print("Grupo no válido.")
        return
    grupos[grupo_elegido]["Campers"].append(estudiante_elegido)
    print(f"Estudiante {estudiante_elegido['nombres']} matriculado en el grupo {grupo_elegido} correctamente.")

    guardar_grupos(grupos)

def asignar_profesor_a_clase():
    clases = cargar_datos2()

    print("Clases disponibles:")
    for clase in clases["clases"]:
        print(f"Clase {clase['nb']}: Duración - {clase['duracion']}")

    while True:
        opcion_clase = input("Ingrese el número de la clase a la que desea asignar un profesor: ")

        try:
            opcion_clase = int(opcion_clase)
            if 1 <= opcion_clase <= len(clases["clases"]):
                clase_elegida = clases["clases"][opcion_clase - 1]
                break
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("\nProfesores disponibles:")
    for i, profesor in enumerate(clases["profesores"], start=1):
        print(f"{i}. {profesor['nombre']} - Rutas: {', '.join(profesor['rutas'])}")

    while True:
        opcion_profesor = input("Ingrese el número del profesor que desea asignar a la clase: ")

        try:
            opcion_profesor = int(opcion_profesor)
            if 1 <= opcion_profesor <= len(clases["profesores"]):
                profesor_elegido = clases["profesores"][opcion_profesor - 1]
                break
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("\nRutas disponibles:")
    for i, ruta in enumerate(clases["rutas"], start=1):
        print(f"{i}. {ruta}")

    while True:
        opcion_ruta = input("Ingrese el número de la ruta que desea asignar al profesor para esta clase: ")

        try:
            opcion_ruta = int(opcion_ruta)
            if 1 <= opcion_ruta <= len(clases["rutas"]):
                ruta_elegida = clases["rutas"][opcion_ruta - 1]
                break
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    profesor_elegido["ruta_asignada"] = ruta_elegida

    clase_elegida["ruta"] = [ruta_elegida]

    print("\nAulas disponibles:")
    for i, aula in enumerate(clases["aulas"], start=1):
        print(f"{i}. {aula}")

    while True:
        opcion_aula = input("Ingrese el número del aula para la clase: ")

        try:
            opcion_aula = int(opcion_aula)
            if 1 <= opcion_aula <= len(clases["aulas"]):
                clase_elegida["aula/s"] = clases["aulas"][opcion_aula - 1]
                break
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    guardar_datos2(clases)
    print(f"Profesor {profesor_elegido['nombre']} asignado a la clase {clase_elegida['nb']} en el aula {clase_elegida['aula/s']} con la ruta {ruta_elegida} correctamente.")



def listar_profesores():
    clases = cargar_datos2()
    print("\nProfesores disponibles:")
    for i, profesor in enumerate(clases["profesores"], start=1):
            print(f"{i}. {profesor['nombre']} - Rutas: {', '.join(profesor['rutas'])}")

import json

def listar_estudiantes_bajo_rendimiento():
    try:
        with open("notas.json", "r", encoding="utf-8") as file:
            datos_notas = json.load(file)

        print("\nEstudiantes con bajo rendimiento:")
        for estudiante in datos_notas:
            for modulo in estudiante.get("modulos", []):
                for nota in modulo.get("notas", []):
                    if nota.get("rendimiento") == "bajo":
                        print(f"Estudiante: {estudiante['nombre']}, Módulo: {modulo['nombre_modulo']}, Rendimiento: Bajo")

    except FileNotFoundError:
        print("Archivo 'notas.json' no encontrado.")
    except Exception as e:
        print(f"Error al cargar y procesar datos: {e}")

def listar_estudiantes_misma_ruta():
    try:
        with open("clases.json", "r", encoding="utf-8") as clases_file:
            datos_clases = json.load(clases_file)

        with open("notas.json", "r", encoding="utf-8") as notas_file:
            datos_notas = json.load(notas_file)

        print("Clases disponibles:")
        for clase in datos_clases["clases"]:
            print(f"{clase['nb']}. Profesor: {clase['profesor']} - Duración: {clase['duracion']} - Ruta: {', '.join(clase['ruta'])}")

        while True:
            opcion_clase = input("Ingrese el número de la clase que desea consultar: ")

            try:
                opcion_clase = int(opcion_clase)
                if 1 <= opcion_clase <= len(datos_clases["clases"]):
                    clase_elegida = datos_clases["clases"][opcion_clase - 1]
                    break
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        profesor_clase = next((profesor for profesor in datos_clases["profesores"] if profesor["nombre"] == clase_elegida["profesor"]), None)

        if profesor_clase:
            ruta_profesor = profesor_clase["ruta_asignada"].lower()

            print(f"\nEstudiantes con la misma ruta que el profesor {profesor_clase['nombre']} (Clase {opcion_clase}):")
            for estudiante in datos_notas:
                for modulo in estudiante.get("modulos", []):
                    for nota in modulo.get("notas", []):
                        ruta_estudio = nota.get("ruta_estudio", "").lower()
                        nombre_modulo = nota.get("nombre_modulo", "")
                        if nombre_modulo in clase_elegida["ruta"] and ruta_estudio == ruta_profesor:
                            print(f"Estudiante: {estudiante['nombre']}, Ruta de Estudio: {ruta_estudio}, Módulo: {nombre_modulo}")
        else:
            print("Error: No se encontró el profesor asignado a la clase.")

    except FileNotFoundError:
        print("Archivos 'clases.json' o 'notas.json' no encontrados.")
    except Exception as e:
        print(f"Error al cargar y procesar datos: {e}")



def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Iniciar Sesión como Coordinador")
    print("2. Iniciar Sesión como Trainer")
    print("3. Iniciar Sesión como Camper")
    print("4. Reportes")
    print("5. Salir del programa")

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
    print("11. Agregar estudiantes a un grupo")
    print("12. Matricular estudiante")
    print("13. Asignar trainer")
    print("14. Salir del programa")

def menu_trainer():
    print("\n--- Menú Trainer ---")
    print("1. Listar todas las clases")
    print("2. Ingresar notas estudiantes inscritos")
    print("3. Salir del programa")

def menu_camper():
    print("\n--- Acceso denegado ---")
    print("Los campers no tienen acceso a este sistema.")

def reportes():
    print("\n--- Reportes ---")
    print("1. Listado de estudiantes inscritos.")
    print("2. Campers aprobaron examen inicial.")
    print("3. Trainers trabajando actualmente.")
    print("4. Campers con bajo rendimiento.")
    print("5. Campers y Trainers que se encuentran en la misma ruta.")
    print("6. Mostrar Campers que aprobaron y reprobaron.")
    print("7. Salir del programa.")

def iniciar_sesion_coordinador():
    while True:
        menu_coordinador()
        opcion = input("\nSeleccione una opción (1-14): ")

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
            listar_estudiantes_aprobados()
        elif opcion == "9":
            listar_estudiantes_reprobados()
        elif opcion == "10":
            listar_clases()
        elif opcion == "11":
            agregar_estudiante_a_grupo()
        elif opcion == "12":
            matricular_estudiantes() 
        elif opcion == "13":
            asignar_profesor_a_clase()
        elif opcion == "14":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1-14).")

def iniciar_sesion_trainer():
    while True:
        menu_trainer()
        opcion = input("\nSeleccione una opción (1-3): ")

        if opcion == "1":
            listar_clases()
        elif opcion == "2":
            listar_estudiantes_inscritos()
            Ti_estudiante = input("Ingrese el TI del estudiante al que desea agregar notas: ")
            agregar_notas_promedio(Ti_estudiante)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1-3).")

def iniciar_sesion_camper():
    menu_camper()

def iniciar_reportes():
    while True:
        reportes()
        opcion = input("\nSeleccione una opción (1-7): ")

        if opcion == "1":
            listar_estudiantes_inscritos()
        elif opcion == "2":
            listar_estudiantes_aprobados()
        elif opcion == "3":
            listar_profesores()
        elif opcion == "4":
            listar_estudiantes_bajo_rendimiento()
        elif opcion == "5":
            listar_estudiantes_misma_ruta()
        elif opcion == "6":
            listar_estudiantes_reprobados()
            print("")
            listar_estudiantes_aprobados()
        elif opcion == "7":
            print ("Saliendo del programa.")
            break
        else:
            print("Opcion no valida. Por favor, ingrese una opcion valida (1-7).")



while True:
    menu_principal()
    opcion = input("\nSeleccione una opción (1-5): ")

    if opcion == "1":
        iniciar_sesion_coordinador()
    elif opcion == "2":
        iniciar_sesion_trainer()
    elif opcion == "3":
        iniciar_sesion_camper()
    elif opcion == "4":
        iniciar_reportes()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1-5).")
