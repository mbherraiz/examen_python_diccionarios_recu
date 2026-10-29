notas = {
    "Garcia": [],
    "Lopez": [],
    "Martinez": [],
    "Rodriguez": [],
    "Gomez": []
}

def ver_todas():
    for alumno, lista in notas.items():
        print(alumno, lista)

def ver_por_alumno():
    apellido = input("Apellido: ").capitalize()

    print(notas.get(apellido, "Alumno no encontrado"))

def cargar_notas():
    apellido = input("Apellido: ").capitalize()
    
    if apellido in notas:
        notas[apellido] = [float(input(f"Nota {i + 1}: ")) for i in range(5)]
    else:
        print("Alumno no encontrado")

def promedio():
    apellido = input("Apellido: ").capitalize()
    
    if apellido in notas and notas[apellido]:
        print(sum(notas[apellido]) / len(notas[apellido]))
    else:
        print("Sin notas o alumno no encontrado")


while True:
    print('''
1. Ver todas las notas
2. Ver notas por alumno
3. Cargar notas
4. Promedio
0. Salir
    ''')
    opcion = str(input("Opción: "))
    match opcion:
        case "1":
            ver_todas()
        case "2":
            ver_por_alumno()
        case "3":
            cargar_notas()
        case "4":
            promedio()
        case "0":
            break
        case _:
            print("Dato incorrecto ingresado, intente nuevamente")