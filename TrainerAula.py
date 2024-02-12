import json

def cargar_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=2)

def imprimir_numeros_clases(clases):
    print("Números de clases disponibles:")
    for clase in clases:
        print(clase['nb'])

def agregar_profesor_aula(clases, profesores, aulas):
    numero_clase = int(input("Ingrese el número de la clase a modificar: "))
    clase_seleccionada = next((clase for clase in clases if clase['nb'] == numero_clase), None)

    if clase_seleccionada:
        imprimir_profesores(profesores)
        nombre_profesor = input("Ingrese el nombre del profesor: ")

        profesor_seleccionado = next((profesor for profesor in profesores if profesor['nombre'] == nombre_profesor), None)

        if profesor_seleccionado:
            clase_seleccionada['profesor'] = nombre_profesor
            clase_seleccionada['ruta'] = profesor_seleccionado['rutas']
            imprimir_aulas(aulas)
            aula = input("Ingrese el nombre del aula: ")
            clase_seleccionada['aula/s'] = aula

            print("Profesor y aula asignados correctamente.")
        else:
            print("Profesor no encontrado.")
    else:
        print("Clase no encontrada.")

def imprimir_profesores(profesores):
    print("Profesores disponibles:")
    for profesor in profesores:
        print(profesor['nombre'])

def imprimir_aulas(aulas):
    print("Aulas disponibles:")
    for aula in aulas:
        print(aula)

nombre_archivo = "clases.json"
datos = cargar_json(nombre_archivo)

clases = datos['clases']
profesores = datos['profesores']
aulas = datos['aulas']

imprimir_numeros_clases(clases)

agregar_profesor_aula(clases, profesores, aulas)

guardar_json(nombre_archivo, datos)