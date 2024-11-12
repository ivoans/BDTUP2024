**Ejercicio 4: Talleres de autos**

**Esquema:**
`TALLER codigoSucursal, domicilioSucursal, telefonoSucursal, codigoFosa, largoFosa, anchoFosa, patenteAuto, marcaAuto, modeloAuto, dniCliente,nombreCliente, celularCliente, dniMecanico, nombreMecanico,emailMecanico`

**Restricciones:**
a. El codigoSucursal corresponde a una sucursal puntual para la cual conocemos el domicilio,teléfono, las fosas que tiene y los mecánicos que trabajan en la misma.

b. De las fosas conocemos el código, el mismo es un número secuencial para cada sucursal (dos sucursales podrían tener el código de fosa 1, pero serían dos fosas distintas). También registramos el largo y ancho de las mismas.

c. En una Fosa se arreglan autos, hay que registrar para cada fosa qué autos se arreglaron en la misma. De los autos conocemos la patente, la marca, el modelo y el cliente que lo acercó.

d. Para un auto registramos un único cliente, pero un cliente puede tener varios autos.

e. Para los clientes registramos el dni, el nombre y el celular.

f. Para los mecánicos registramos el dni, el nombre y el email.

### 1) Determinar las dependencias funcionales
    La Sucursal la identificamos con el codigoSucursal, y sus atributos pueden ser: domicilioSucursal y telefonoSucursal.

    Una Fosa de una sucursal la identificamos con: codigoSucursal + codigoFosa. Y tiene largoFosa y anchoFosa.

    Un Auto se identifica por patenteAuto, con los atributos marcaAuto, modeloAuto, y dniCliente.

    El Cliente se identifica por dniCliente, con los atributos nombreCliente y celularCliente.

    Al mecanico se lo puede identificar con su dni (dniMecanico) y con sus atributos: nombreMecanico, mailMecanico

    Por cada reparación hay que registrar: codigoSucursal, codigoFosa, patenteAuto, y dniMecanico.

### 2) Eleccion de primary key

Sucursal: `codigoSucursal` ya que puede ser autoincremental y es unica por cada sucursal.

Fosa: (`codigoSucursal` + `codigoFosa`) tienen que ser esas dos porque el codigo fosa se puede repetir en las distintas sucursales, pero es unico por cada sucursal.

Auto: `patenteAuto` porque la patente es unica

Cliente: `dniCliente` porque el dni es unico por cada persona

Mecanico: `dniMecanico` porque al igual que en cliente el dni es unico por persona

Reparacion: `dniMecanico, codigoSucursal, codigoFosa, patenteAuto y dniCliente` ya que son todas las pk de cada entidad y siempre va a indicar exactamente a cual corresponde corresponde, osea que identifica de forma unica a cada reparacion.

### 3) Normalizacion hasta 3NF

Para que este esquema llegue a la **Tercer Forma Normal(3NF)** organizamos la tabla en todas entidades independientes, asi se eliminan independencias transitivas y se garantiza que cada atributo no clave dependa únicamente de la clave primaria completa.

El nuevo diseño en 3FN sería el siguiente:

1. **Tabla `Sucursal`**
   - `codigoSucursal` (Primary key)
   - `domicilioSucursal`
   - `telefonoSucursal`

2. **Tabla `Fosa`**
   - `codigoSucursal` (Foreign key que referencia a `Sucursal`)
   - `nombreGaleria` (Primary key compuesta junto con `codigoSucursal`)
   - `largoFosa`
   - `anchoFosa`

3. **Tabla `Auto`**
   - `patenteAuto` (Priamry key)
   - `marcaAuto`
   - `modeloAuto`
   - `dniCliente` (Foreign key que referenia a `Cliente`)

4. **Tabla `Cliente`**
   - `dniCliente` (Primary key)
   - `nombreCliente`
   - `celularCliente`

5. **Tabla `Mecanico`**
   - `dniMecanico` (Primary key)
   - `nombreMecanico`
   - `emailMecanico`

6. **Tabla `Reparacion`**
   - `codigoSucursal` (Foreign key que referenia a `Sucursal`)
   - `cosdigoFosa`  (Foreign key que referenia a `Fosa`)
   - `patenteAuto` (Foreign key que referenia a `Auto`)
   - `dniMecanico` (Foreign key que referenia a `Mecanico`)
   - (Primary key compuesta: (`codigoSucursal`,`cosdigoFosa`, `patenteAuto`, `dniMecanico`))