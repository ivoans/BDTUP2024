from conexion import registrarMedico, consultarMedico, modificarMedico, listarMedicos, eliminarMedico, consultarPorID, consultarPorEspecialidad, consultarPorApellido

def menuMedico():
    opcion = 0
    while opcion != 6:
        print("----------MENU MEDICOS----------")
        print("1. Registrar Medico")
        print("2. Consultar Medico")
        print("3. Modificar Medico")
        print("4. Listar Medicos")
        print("5. Eliminar Medico")
        print("6. Salir")
        print("----------------------------------")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            dni = int(input("Ingrese DNI: "))
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            especialidad = input("Ingrese especialidad: ")
            mail = input("Ingrese mail: ")
            registrarMedico(dni, nombre, apellido, especialidad, mail)
        elif opcion == 2:
            consultarMedicos()
        elif opcion == 3:
            dni = int(input("Ingrese DNI: "))
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            especialidad = input("Ingrese especialidad: ")
            mail = input("Ingrese mail: ")
            modificarMedico(dni, nombre, apellido, especialidad, mail)
        elif opcion == 4:
            listarMedicos()
        elif opcion == 5:
            dni = int(input("Ingrese DNI: "))
            eliminarMedico(dni)
        elif opcion == 6:
            print("Saliendo...")
        else:
            print("Opción inválida.")

def consultarMedicos():
    opcion = 0
    while opcion != 5:
        print("----------CONSULTAR MEDICOS----------")
        print("1. Consultar por DNI")
        print("2. Consultar por ID")
        print("3. Consultar por Apellido")
        print("4. Consultar por Especialidad")
        print("5. Salir")
        print("----------------------------------")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            dni = int(input("Ingrese DNI: "))
            consultarMedico(dni)
        elif opcion == 2:
            ID = int(input("Ingrese ID: "))
            consultarPorID(ID)
        elif opcion == 3:
            apellido = input("Ingrese Apellido: ")
            consultarPorApellido(apellido)
        elif opcion == 4:
            especialidad = input("Ingrese Especialidad: ")
            consultarPorEspecialidad(especialidad)
        elif opcion == 5:
            print("Saliendo...")
        else:
            print("Opción inválida.")
