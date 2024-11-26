import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234abcd",
        database="proyectofinal"
    )
    
    if conexion.is_connected():
        print("Conexión exitosa a la base de datos.")

    cursor = conexion.cursor()

    # Pacientes
    def registrarPaciente(dni, nombre, apellido, fecha_nacimiento, mail):
        try:
            cursor.execute("INSERT INTO pacientes (dni, nombre, apellido, fecha_nacimiento, mail) VALUES (%s, %s, %s, %s, %s)", (dni, nombre, apellido, fecha_nacimiento, mail))
            conexion.commit()
            print("Paciente registrado con éxito.")
        except mysql.connector.Error as error:
            print("Error al registrar paciente: {}".format(error))

    def consultarPaciente(dni):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE dni = %s", (dni,))
            paciente = cursor.fetchone()
            if paciente:
                print("ID: ", paciente[0])
                print("DNI: ", paciente[1])
                print("Nombre: ", paciente[2])
                print("Apellido: ", paciente[3])
                print("Fecha de nacimiento: ", paciente[4])
                print("Mail: ", paciente[5])
                print("------------------------")
            else:
                print("Paciente no encontrado.")
        except mysql.connector.Error as error:
            print("Error al consultar paciente: {}".format(error))

    def consultarPacientePorID(ID):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE id = %s", (ID,))
            paciente = cursor.fetchone()
            if paciente:
                print("ID: ", paciente[0])
                print("DNI: ", paciente[1])
                print("Nombre: ", paciente[2])
                print("Apellido: ", paciente[3])
                print("Fecha de nacimiento: ", paciente[4])
                print("Mail: ", paciente[5])
            else:
                print("Paciente no encontrado.")
        except mysql.connector.Error as error:
            print("Error al consultar paciente: {}".format(error))

    def consultarPacientePorApellido(apellido):
        try:
            cursor.execute("SELECT * FROM pacientes WHERE apellido = %s", (apellido,))
            pacientes = cursor.fetchall()
            if pacientes:
                for paciente in pacientes:
                    print("ID: ", paciente[0])
                    print("DNI: ", paciente[1])
                    print("Nombre: ", paciente[2])
                    print("Apellido: ", paciente[3])
                    print("Fecha de nacimiento: ", paciente[4])
                    print("Mail: ", paciente[5])
                    print("------------------------")
            else:
                print("Paciente no encontrado.")
        except mysql.connector.Error as error:
            print("Error al consultar paciente: {}".format(error))

    def modificarPaciente(dni, nombre, apellido, fecha_nacimiento, mail):
        try:
            cursor.execute("UPDATE pacientes SET nombre = %s, apellido = %s, fecha_nacimiento = %s, mail = %s WHERE dni = %s", (nombre, apellido, fecha_nacimiento, mail, dni))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró un paciente con el DNI proporcionado.")
            else:
                print("Paciente modificado con éxito.")
        except mysql.connector.Error as error:
            print("Error al modificar paciente: {}".format(error))


    def listarPacientes():
        try:
            cursor.execute("SELECT * FROM pacientes")
            pacientes = cursor.fetchall()
            if pacientes:
                for paciente in pacientes:
                    print("ID: ", paciente[0])
                    print("DNI: ", paciente[1])
                    print("Nombre: ", paciente[2])
                    print("Apellido: ", paciente[3])
                    print("Fecha de nacimiento: ", paciente[4])
                    print("Mail: ", paciente[5])
                    print("------------------------")
            else:
                print("No hay pacientes registrados.")
        except mysql.connector.Error as error:
            print("Error al listar pacientes: {}".format(error))

    def eliminarPaciente(dni):
        try:
            cursor.execute("DELETE FROM pacientes WHERE dni = %s", (dni,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró un paciente con el DNI proporcionado.")
            else:
                print("Paciente eliminado con éxito.")
        except mysql.connector.Error as error:
            print("Error al eliminar paciente: {}".format(error))

    # Medicos
    def registrarMedico(dni, nombre, apellido, especialidad, mail):
        try:
            cursor.execute("INSERT INTO medicos (dni, nombre, apellido, especialidad, mail) VALUES (%s, %s, %s, %s, %s)", (dni, nombre, apellido, especialidad, mail))
            conexion.commit()
            print("Médico registrado con éxito.")
        except mysql.connector.Error as error:
            print("Error al registrar médico: {}".format(error))

    def consultarMedico(dni):
        try:
            cursor.execute("SELECT * FROM medicos WHERE dni = %s", (dni,))
            medico = cursor.fetchone()
            if medico:
                print("ID: ", medico[0])
                print("DNI: ", medico[1])
                print("Nombre: ", medico[2])
                print("Apellido: ", medico[3])
                print("Especialidad: ", medico[4])
                print("Mail: ", medico[5])
                print("------------------------")
            else:
                print("Médico no encontrado.")
        except mysql.connector.Error as error:
            print("Error al consultar médico: {}".format(error))

    def consultarPorID(ID):
        try:
            cursor.execute("SELECT * FROM medicos WHERE id = %s", (ID,))
            medico = cursor.fetchone()
            if medico:
                print("ID: ", medico[0])
                print("DNI: ", medico[1])
                print("Nombre: ", medico[2])
                print("Apellido: ", medico[3])
                print("Especialidad: ", medico[4])
                print("Mail: ", medico[5])
            else:
                print("Médico no encontrado.")
        except mysql.connector.Error as error:
            print("Error al consultar médico: {}".format(error))

    def consultarPorApellido(apellido):
        try:
            cursor.execute("SELECT * FROM medicos WHERE apellido = %s", (apellido,))
            medicos = cursor.fetchall()
            if medicos:
                for medico in medicos:
                    print("ID: ", medico[0])
                    print("DNI: ", medico[1])
                    print("Nombre: ", medico[2])
                    print("Apellido: ", medico[3])
                    print("Especialidad: ", medico[4])
                    print("Mail: ", medico[5])
                    print("------------------------")
            else:
                print("Médico no encontrado.")
        except mysql.connector.Error as error:
            print("Error al consultar médico: {}".format(error))

    def consultarPorEspecialidad(especialidad):
        try:
            cursor.execute("SELECT * FROM medicos WHERE especialidad = %s", (especialidad,))
            medicos = cursor.fetchall()
            if medicos:
                for medico in medicos:
                    print("ID: ", medico[0])
                    print("DNI: ", medico[1])
                    print("Nombre: ", medico[2])
                    print("Apellido: ", medico[3])
                    print("Especialidad: ", medico[4])
                    print("Mail: ", medico[5])
                    print("------------------------")
            else:
                print("Médico no encontrado.")
        except mysql.connector.Error as error:
            print("Error al consultar médico: {}".format(error))


    def modificarMedico(dni, nombre, apellido, especialidad, mail):
        try:
            cursor.execute("UPDATE medicos SET nombre = %s, apellido = %s, especialidad = %s, mail = %s WHERE dni = %s", (nombre, apellido, especialidad, mail, dni))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró un medico con el DNI proporcionado.")
            else:
                print("Medico modificado con éxito.")
        except mysql.connector.Error as error:
            print("Error al modificar médico: {}".format(error))

    def eliminarMedico(dni):
        try:
            cursor.execute("DELETE FROM medicos WHERE dni = %s", (dni,))
            conexion.commit()
            if cursor.rowcount == 0:
                print("No se encontró un medico con el DNI proporcionado.")
            else:
                print("Medico eliminado con éxito.")
        except mysql.connector.Error as error:
            print("Error al eliminar médico: {}".format(error))

    def listarMedicos():
        try:
            cursor.execute("SELECT * FROM medicos")
            medicos = cursor.fetchall()
            if medicos:
                for medico in medicos:
                    print("DNI: ", medico[0])
                    print("Nombre: ", medico[1])
                    print("Apellido: ", medico[2])
                    print("Especialidad: ", medico[3])
                    print("Mail: ", medico[4])
                    print("------------------------")
            else:
                print("No hay médicos registrados.")
        except mysql.connector.Error as error:
            print("Error al listar médicos: {}".format(error))

    # Turnos
    def registrarTurno(paciente_ID, medico_ID, fecha, hora):
        try:
            cursor.execute("INSERT INTO turnos (paciente_ID, medico_ID, fecha, hora) VALUES (%s, %s, %s, %s)", (paciente_ID, medico_ID, fecha, hora))
            conexion.commit()
            print("Turno registrado con éxito.")
        except mysql.connector.Error as error:
            print("Error al registrar turno: {}".format(error))

    def consultarTurnoPorPaciente(paciente_ID):
        try:
            cursor.execute("SELECT * FROM turnos WHERE paciente_ID = %s", (paciente_ID,))
            turnos = cursor.fetchall()
            if turnos:
                for turno in turnos:
                    print("ID: ", turno[0])
                    print("Paciente ID: ", turno[1])
                    print("Médico ID: ", turno[2])
                    print("Fecha: ", turno[3])
                    print("Hora: ", turno[4])
                    print("------------------------")
            else:
                print("No hay turnos registrados para ese paciente.")
        except mysql.connector.Error as error:
            print("Error al consultar turno: {}".format(error))

    def consultarTurnoPorMedico(medico_ID):
        try:
            cursor.execute("SELECT * FROM turnos WHERE medico_ID = %s", (medico_ID,))
            turnos = cursor.fetchall()
            if turnos:
                for turno in turnos:
                    print("ID: ", turno[0])
                    print("Paciente ID: ", turno[1])
                    print("Médico ID: ", turno[2])
                    print("Fecha: ", turno[3])
                    print("Hora: ", turno[4])
                    print("------------------------")
            else:
                print("No hay turnos registrados para ese médico.")
        except mysql.connector.Error as error:
            print("Error al consultar turno: {}".format(error))

    def modificarTurno(ID, paciente_ID, medico_ID, fecha, hora):
        try:
            cursor.execute("UPDATE turnos SET paciente_ID = %s, medico_ID = %s, fecha = %s, hora = %s WHERE ID = %s", (paciente_ID, medico_ID, fecha, hora, ID))
            conexion.commit()
            print("Turno modificado con éxito.")
        except mysql.connector.Error as error:
            print("Error al modificar turno: {}".format(error))

    def listarTurnos():
        try:
            cursor.execute("SELECT * FROM turnos")
            turnos = cursor.fetchall()
            if turnos:
                for turno in turnos:
                    print("ID: ", turno[0])
                    print("Paciente ID: ", turno[1])
                    print("Médico ID: ", turno[2])
                    print("Fecha: ", turno[3])
                    print("Hora: ", turno[4])
                    print("------------------------")
            else:
                print("No hay turnos registrados.")
        except mysql.connector.Error as error:
            print("Error al listar turnos: {}".format(error))

    def eliminarTurno(ID):
        try:
            cursor.execute("DELETE FROM turnos WHERE ID = %s", (ID,))
            conexion.commit()
            print("Turno eliminado con éxito.")
        except mysql.connector.Error as error:
            print("Error al eliminar turno: {}".format(error))

    def pacientesConMasTurnos():
        try:
            cursor.execute("SELECT pacientes.ID, pacientes.nombre, pacientes.DNI, COUNT(turnos.ID) AS cantidad FROM pacientes JOIN turnos ON pacientes.ID = turnos.paciente_ID GROUP BY pacientes.ID ORDER BY cantidad DESC LIMIT 3")
            pacientes = cursor.fetchall()
            if pacientes:
                for paciente in pacientes:
                    print("ID: ", paciente[0])
                    print("Nombre: ", paciente[1])
                    print("DNI: ", paciente[2])
                    print("Cantidad de turnos: ", paciente[3])
                    print("------------------------")
            else:
                print("No hay pacientes registrados.")
        except mysql.connector.Error as error:
            print("Error al listar pacientes: {}".format(error))

    def medicosConMasTurnos():
        try:
            cursor.execute("SELECT medicos.ID, medicos.nombre, medicos.DNI, COUNT(turnos.ID) AS cantidad FROM medicos JOIN turnos ON medicos.ID = turnos.medico_ID GROUP BY medicos.ID ORDER BY cantidad DESC LIMIT 3")
            medicos = cursor.fetchall()
            if medicos:
                for medico in medicos:
                    print("ID: ", medico[0])
                    print("Nombre: ", medico[1])
                    print("DNI: ", medico[2])
                    print("Cantidad de turnos: ", medico[3])
                    print("------------------------")
            else:
                print("No hay médicos registrados.")
        except mysql.connector.Error as error:
            print("Error al listar médicos: {}".format(error))

    def cerrarConexion():
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")


except mysql.connector.Error as error:
    print("Error al conectar a la base de datos: {}".format(error))
