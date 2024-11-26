from conexion import registrarPaciente, consultarPaciente, modificarPaciente, listarPacientes, eliminarPaciente, consultarPacientePorID, consultarPacientePorApellido

def menuPaciente():
    opcion = 0
    while opcion != 6:
        print("----------MENU PACIENTES----------")
        print("1. Registrar Paciente")
        print("2. Consultar Paciente")
        print("3. Modificar Paciente")
        print("4. Listar Pacientes")
        print("5. Eliminar Paciente")
        print("6. Salir")
        print("----------------------------------")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            dni = int(input("Ingrese DNI: "))
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (AAAA-MM-DD): ")
            mail = input("Ingrese mail: ")
            registrarPaciente(dni, nombre, apellido, fecha_nacimiento, mail)
        elif opcion == 2:
            consultarPacientes()
        elif opcion == 3:
            dni = int(input("Ingrese DNI: "))
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (AAAA-MM-DD): ")
            mail = input("Ingrese mail: ")
            modificarPaciente(dni, nombre, apellido, fecha_nacimiento, mail)
        elif opcion == 4:
            listarPacientes()
        elif opcion == 5:
            dni = int(input("Ingrese DNI: "))
            eliminarPaciente(dni)
        elif opcion == 6:
            print("Saliendo...")
        else:
            print("Opción inválida.")

def consultarPacientes():
    opcion = 0
    while opcion != 4:
        print("----------CONSULTAR PACIENTES----------")
        print("1. Consultar por DNI")
        print("2. Consultar por ID")
        print("3. Consultar por Apellido")
        print("4. Salir")
        print("----------------------------------")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            dni = int(input("Ingrese DNI: "))
            consultarPaciente(dni)
        elif opcion == 2:
            ID = int(input("Ingrese ID: "))
            consultarPacientePorID(ID)
        elif opcion == 3:
            apellido = input("Ingrese Apellido: ")
            consultarPacientePorApellido(apellido)
        elif opcion == 4:
            print("Saliendo...")
        else:
            print("Opción inválida.")