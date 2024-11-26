from menu.menuMedicos import menuMedico
from menu.menuPacientes import menuPaciente
from menu.menuTurnos import menuTurno
from conexion import cerrarConexion

def main():
    opcion = 0
    while opcion != 4:
        print("----------MENU----------")
        print("1. Pacientes")
        print("2. Medicos")
        print("3. Turnos")
        print("4. Salir")
        print("------------------------")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            menuPaciente()
        elif opcion == 2:
            menuMedico()
        elif opcion == 3:
            menuTurno()
        elif opcion == 4:
            print("Saliendo...")
            cerrarConexion()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()