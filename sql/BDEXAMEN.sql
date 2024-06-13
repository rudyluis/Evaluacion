CREATE TABLE estudiantes (
    id_estudiante SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_nacimiento date,
    direccion VARCHAR(255),
    carrera VARCHAR(100)
);

INSERT INTO estudiantes (nombre, fecha_nacimiento, direccion, carrera) VALUES
('Juan Pérez', '2000-01-01', 'Calle 123', 'Ingeniería de Sistemas'),
('Ana Gómez', '2001-12-05', 'Calle 456', 'Ingeniería de Sistemas'),
('Luis Martínez', '2002-06-06', 'Calle 789', 'Medicina'),
('María Rodríguez', '2003-05-07', 'Calle 101', 'Derecho');


CREATE TABLE profesor (
    id_profesor SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    departamento VARCHAR(100),
    salario DECIMAL(10, 2)
);

INSERT INTO profesor (nombre, departamento, salario) VALUES
('Carlos Sánchez', 'Ingeniería', 4000.00),
('Laura Ruiz', 'Medicina', 4500.00),
('Pedro Jiménez', 'Derecho', 4200.00),
('Marta López', 'Ingeniería', 4300.00);

CREATE TABLE curso (
    id_curso SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    id_profesor INT REFERENCES profesor(id_profesor),
    semestre VARCHAR(10)
);

INSERT INTO curso (nombre, id_profesor, semestre) VALUES
('Matemáticas', 1, '2023-1'),
('Biología', 2, '2023-1'),
('Derecho Civil', 3, '2023-1'),
('Programación', 4, '2023-1');


CREATE TABLE inscripcion (
    id_inscripcion SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    id_curso INT REFERENCES curso(id_curso),
    nota DECIMAL(18, 2)
);

INSERT INTO inscripcion(id_estudiante, id_curso, nota) VALUES
(1, 1, 85.5),
(2, 4, 92.0),
(3, 2, 78.0),
(4, 3, 88.0),
(1, 4, 95.0);