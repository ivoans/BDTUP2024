use proyectofinal;

-- CREACION DE TABLAS INICIALES

CREATE TABLE Pacientes(
	ID INT NOT NULL auto_increment,
    DNI INT NOT NULL UNIQUE,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    mail VARCHAR(100) NOT NULL,
    PRIMARY KEY(ID)
);

CREATE TABLE Medicos(
	ID INT NOT NULL auto_increment,
    DNI INT NOT NULL UNIQUE,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    mail VARCHAR(100) NOT NULL,
    PRIMARY KEY(ID)
);

CREATE TABLE Turnos(
	ID INT NOT NULL AUTO_INCREMENT,
    paciente_ID INT NOT NULL,
    medico_ID INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (paciente_ID) REFERENCES Pacientes(ID) ON DELETE CASCADE,
    FOREIGN KEY (medico_ID) REFERENCES Medicos(ID) ON DELETE CASCADE
);


-- INSERTS INICIALES

INSERT INTO Pacientes (DNI, nombre, apellido, fecha_nacimiento, mail)
VALUES
(12345678, 'Juan', 'Pérez', '1980-01-15', 'juan.perez@mail.com'),
(23456789, 'María', 'Gómez', '1985-03-22', 'maria.gomez@mail.com'),
(34567890, 'Carlos', 'López', '1990-07-10', 'carlos.lopez@mail.com'),
(45678901, 'Ana', 'Martínez', '1992-11-05', 'ana.martinez@mail.com'),
(56789012, 'Luis', 'Fernández', '1978-02-28', 'luis.fernandez@mail.com'),
(67890123, 'Laura', 'Díaz', '1988-09-17', 'laura.diaz@mail.com'),
(78901234, 'Pedro', 'Sánchez', '1995-12-13', 'pedro.sanchez@mail.com'),
(89012345, 'Marta', 'Rodríguez', '1983-06-19', 'marta.rodriguez@mail.com'),
(90123456, 'Jorge', 'Torres', '1975-08-23', 'jorge.torres@mail.com'),
(12345098, 'Sofía', 'Ramírez', '1999-04-30', 'sofia.ramirez@mail.com');

INSERT INTO Medicos (DNI, nombre, apellido, especialidad, mail)
VALUES
(11111111, 'Dr. Sebastián', 'Muñoz', 'Cardiología', 'sebastian.munoz@mail.com'),
(22222222, 'Dra. Carolina', 'Vargas', 'Pediatría', 'carolina.vargas@mail.com'),
(33333333, 'Dr. Alberto', 'García', 'Dermatología', 'alberto.garcia@mail.com'),
(44444444, 'Dra. Natalia', 'Ortega', 'Neurología', 'natalia.ortega@mail.com'),
(55555555, 'Dr. Ricardo', 'Álvarez', 'Traumatología', 'ricardo.alvarez@mail.com'),
(66666666, 'Dra. Elena', 'Salinas', 'Ginecología', 'elena.salinas@mail.com'),
(77777777, 'Dr. Andrés', 'Hernández', 'Oftalmología', 'andres.hernandez@mail.com'),
(88888888, 'Dra. Clara', 'Ruiz', 'Psicología', 'clara.ruiz@mail.com'),
(99999999, 'Dr. Hugo', 'Castro', 'Oncología', 'hugo.castro@mail.com'),
(12121212, 'Dra. Cecilia', 'Morales', 'Urología', 'cecilia.morales@mail.com');

INSERT INTO Turnos (paciente_ID, medico_ID, fecha, hora) VALUES
(1, 3, '2024-11-25', '09:00:00'),
(2, 5, '2024-11-26', '10:30:00'),
(3, 7, '2024-11-27', '11:15:00'),
(4, 2, '2024-11-28', '14:00:00'),
(5, 6, '2024-11-29', '08:45:00'),
(6, 1, '2024-11-30', '09:30:00'),
(7, 9, '2024-12-01', '10:00:00'),
(8, 4, '2024-12-02', '11:45:00'),
(9, 8, '2024-12-03', '13:15:00'),
(10, 10, '2024-12-04', '15:00:00'),
(1, 6, '2024-12-05', '09:15:00'),
(2, 8, '2024-12-06', '10:45:00'),
(3, 2, '2024-12-07', '11:30:00'),
(4, 7, '2024-12-08', '08:30:00'),
(5, 3, '2024-12-09', '09:00:00'),
(6, 10, '2024-12-10', '10:15:00'),
(7, 1, '2024-12-11', '11:00:00'),
(8, 5, '2024-12-12', '12:30:00'),
(9, 4, '2024-12-13', '13:45:00'),
(10, 9, '2024-12-14', '14:15:00'),
(1, 4, '2024-12-15', '09:30:00'),
(2, 7, '2024-12-16', '10:15:00'),
(3, 1, '2024-12-17', '11:00:00'),
(4, 10, '2024-12-18', '08:45:00'),
(5, 2, '2024-12-19', '09:15:00'),
(6, 8, '2024-12-20', '10:30:00'),
(7, 3, '2024-12-21', '11:45:00'),
(8, 6, '2024-12-22', '13:00:00'),
(9, 5, '2024-12-23', '14:15:00'),
(10, 9, '2024-12-24', '15:00:00'),
(1, 5, '2024-12-26', '09:00:00'),
(2, 6, '2024-12-27', '10:30:00'),
(3, 7, '2024-12-28', '11:00:00'),
(4, 8, '2024-12-29', '08:45:00'),
(5, 9, '2024-12-30', '09:15:00'),
(6, 10, '2024-12-31', '10:00:00'),
(7, 1, '2025-01-02', '11:30:00'),
(8, 2, '2025-01-03', '12:45:00'),
(9, 3, '2025-01-04', '13:15:00'),
(10, 4, '2025-01-05', '14:00:00'),
(1, 6, '2025-01-06', '09:00:00'),
(2, 8, '2025-01-07', '10:15:00'),
(3, 9, '2025-01-08', '11:30:00'),
(4, 10, '2025-01-09', '08:45:00'),
(5, 7, '2025-01-10', '09:15:00'),
(6, 5, '2025-01-11', '10:00:00'),
(7, 4, '2025-01-12', '11:45:00'),
(8, 3, '2025-01-13', '12:30:00'),
(9, 2, '2025-01-14', '13:15:00'),
(10, 1, '2025-01-15', '14:30:00'),
(1, 2, '2025-01-16', '09:00:00'),
(2, 4, '2025-01-17', '10:15:00'),
(3, 6, '2025-01-18', '11:00:00'),
(4, 8, '2025-01-19', '12:00:00'),
(5, 10, '2025-01-20', '09:45:00'),
(6, 7, '2025-01-21', '10:30:00'),
(7, 5, '2025-01-22', '11:15:00'),
(8, 3, '2025-01-23', '13:00:00'),
(9, 1, '2025-01-24', '14:15:00'),
(10, 9, '2025-01-25', '15:00:00'),
(3, 7, '2025-01-26', '09:00:00'),
(8, 4, '2025-01-27', '10:30:00'),
(5, 9, '2025-01-28', '11:15:00'),
(2, 6, '2025-01-29', '08:45:00'),
(10, 1, '2025-01-30', '09:45:00'),
(6, 8, '2025-01-31', '10:00:00'),
(1, 5, '2025-02-01', '11:30:00'),
(4, 3, '2025-02-02', '12:00:00'),
(7, 10, '2025-02-03', '13:15:00'),
(9, 2, '2025-02-04', '14:00:00'),
(8, 9, '2025-02-05', '09:30:00'),
(3, 5, '2025-02-06', '10:45:00'),
(6, 2, '2025-02-07', '11:15:00'),
(1, 4, '2025-02-08', '12:45:00'),
(10, 7, '2025-02-09', '08:30:00'),
(2, 1, '2025-02-10', '09:15:00'),
(5, 6, '2025-02-11', '10:30:00'),
(7, 8, '2025-02-12', '11:45:00'),
(4, 3, '2025-02-13', '13:00:00'),
(9, 10, '2025-02-14', '14:30:00');