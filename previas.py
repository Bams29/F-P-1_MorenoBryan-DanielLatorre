import json

# Función para cargar datos de estudiantes desde un archivo JSON
def cargar_estudiantes(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return []

# Función para buscar un estudiante en la lista de estudiantes
def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        if estudiante['nombres'] == nombre:
            return estudiante
    return None

# Función para guardar las notas en un archivo JSON
def guardar_notas(notas):
    with open('notas.json', 'w') as archivo:
        json.dump(notas, archivo)

# Función principal
def main():
    # Cargar datos de estudiantes
    estudiantes = cargar_estudiantes('estudiantes.json')

    # Solicitar nombre del estudiante a buscar
    nombre_estudiante = input("Ingrese el nombre del estudiante a buscar: ")

    # Buscar al estudiante
    estudiante = buscar_estudiante(estudiantes, nombre_estudiante)

    if estudiante:
        # Solicitar las notas
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))

        # Solicitar la ruta de estudio
        ruta_estudio = input("Ingrese la ruta de estudio: ")

        # Calcular porcentajes
        nota1 *= 0.1
        nota2 *= 0.3
        nota3 *= 0.6

        # Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Guardar las notas en un archivo JSON
        notas = {
            "nombre": nombre_estudiante,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "promedio": promedio,
            "ruta_estudio": ruta_estudio
        }
        guardar_notas(notas)

        print("Notas guardadas exitosamente.")
    else:
        print("Estudiante no encontrado.")

if __name__ == "__main__":
    main()
