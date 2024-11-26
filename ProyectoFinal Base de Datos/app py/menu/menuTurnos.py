from conexion import registrarTurno, consultarTurnoPorPaciente, consultarTurnoPorMedico, modificarTurno, listarTurnos, eliminarTurno, pacientesConMasTurnos, medicosConMasTurnos

def menuTurno():
    opcion = 0
    while opcion != 9:
        print("----------MENU TURNOS----------")
        print("1. Registrar Turno")
        print("2. Consultar Turno por paciente")
        print("3. Consultar Turno por médico")
        print("4. Modificar Turno")
        print("5. Listar Turnos")
        print("6. Eliminar Turno")
        print("7. Pacientes con más turnos")
        print("8. Médicos con más turnos")
        print("9. Salir")
        print("----------------------------------")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            paciente_ID = int(input("Ingrese el ID del paciente: "))
            medico_ID = int(input("Ingrese el ID del médico: "))
            fecha = input("Ingrese la fecha (AAAA-MM-DD): ")
            hora = input("Ingrese la hora (HH:MM): ")
            registrarTurno(paciente_ID, medico_ID, fecha, hora)
        elif opcion == 2:
            paciente_ID = int(input("Ingrese el ID del paciente: "))
            consultarTurnoPorPaciente(paciente_ID)
        elif opcion == 3:
            medico_ID = int(input("Ingrese el ID del médico: "))
            consultarTurnoPorMedico(medico_ID)
        elif opcion == 4:
            turno_ID = int(input("Ingrese el ID del turno: "))
            paciente_ID = int(input("Ingrese el ID del paciente: "))
            medico_ID = int(input("Ingrese el ID del médico: "))
            fecha = input("Ingrese la fecha (AAAA-MM-DD): ")
            hora = input("Ingrese la hora (HH:MM): ")
            modificarTurno(turno_ID, paciente_ID, medico_ID, fecha, hora)
        elif opcion == 5:
            listarTurnos()
        elif opcion == 6:
            turno_ID = int(input("Ingrese el ID del turno: "))
            eliminarTurno(turno_ID)
        elif opcion == 7:
            pacientesConMasTurnos()
        elif opcion == 8:
            medicosConMasTurnos()
        elif opcion == 9:
            print("Saliendo...")
        else:
            print("Opción inválida")