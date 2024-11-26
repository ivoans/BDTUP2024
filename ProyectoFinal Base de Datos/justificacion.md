**Sistema de Gestión De un Hospital**

**Esquema inicial:** `HOSPITAL Paciente(idPaciente, dniPaciente, nombrePaciente, apellidoPaciente, fechaNacimientoPaciente, mailPaciente), Medico(idMedico, dniMedico, nombreMedico, apellidoMedico, especialidadMedico, mailMedico), Turno(idTurno, idPaciente, idMedico, fechaTurno, horaTurno)`

**Restricciones:**
a. Cada paciente está identificado por su IDe, y se registran datos como su nombre, apellido, fecha de nacimiento y correo electrónico.
Un dniPaciente es único para cada persona.

b. Cada médico está identificado por su ID, y se registran datos como su especialidad y correo electrónico.
Un dniMedico es único para cada médico.

c. Un turno corresponde a una consulta médica, vinculando a un paciente con un médico con cada ID correspondiente en una fecha y hora específicas.
Cada turno se identifica con un ID único.

### 1) Determinar las dependencias funcionales

    Medico, Paciente y Turno dependen de su ID propio, ademas tambien, medico y paciente
    tienen un dni unico que no se puede repetir al igual que el ID.

### 2) Eleccion de primary key

Paciente: `idPaciente` (primary key) porque identifica de manera única a cada paciente.

Medico: `idMedico` (primary key) porque identifica de manera única a cada médico.

Turno: `idTurno` (primary key) porque identifica de manera unica a cada turno.

### 3) Normalizacion hasta 3NF

Para que este esquema llegue a la **Tercer Forma Normal(3NF)** organizamos la tabla en todas entidades independientes, asi se eliminan independencias transitivas y se garantiza que cada atributo no clave dependa únicamente de la clave primaria completa.

El nuevo diseño en 3FN sería el siguiente:
1. **Tabla `Pacientes`**
   - `ID` (Primary key)
   - `DNI` (Unique)
   - `nombre`
   - `apellido`
   - `fecha_nacimiento`
   - `mail`

2. **Tabla `Medicos`**
   - `ID` (Foreign key que referencia a `Sucursal`)
   - `DNI` (Unique)
   - `nombre`
   - `apellido`
   - `especioalidad`
   - `mail`

3. **Tabla `Turnos`**
   - `ID` (Priamry key)
   - `pacienteID` (Foreign key que referenia a `Pacientes`)
   - `medicoID` (Foreign key que referenia a `Medicos`)
   - `fecha`
   - `hora`

### Justificación:
1. Primera Forma Normal (1FN):
Todas las tablas tienen valores atómicos, sin grupos repetidos ni listas de valores en celdas.

2. Segunda Forma Normal (2FN):
Todas las tablas están en 1FN, y los atributos no clave dependen completamente de la pk.

3. Tercer Forma Normal (3FN):
No existen dependencias transitivas, se asegura que todos los atributos no clave dependan directamente de la pk sin depender de otros atributos no clave.
