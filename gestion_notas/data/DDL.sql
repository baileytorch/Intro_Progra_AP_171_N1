CREATE TABLE IF NOT EXISTS docentes(
    id_docente INT AUTO_INCREMENT,
    rut_docente INT NOT NULL UNIQUE,
    digito_ver VARCHAR(1) NOT NULL,
    nombre_docente VARCHAR(250) NOT NULL,
    email_docente VARCHAR(250) NULL,
    
    CONSTRAINT pk_docentes PRIMARY KEY (id_docente)
);

CREATE TABLE IF NOT EXISTS asignaturas(
    id_asignatura INT AUTO_INCREMENT,
    codigo_asig VARCHAR(6) NOT NULL UNIQUE,
    nombre_asig VARCHAR(250) NOT NULL,
    descripcion_asig VARCHAR(250) NULL,
    
    CONSTRAINT pk_asignaturas PRIMARY KEY (id_asignatura)
);

CREATE TABLE IF NOT EXISTS docentes_asignaturas(
    id_docente_asignatura INT AUTO_INCREMENT,
    id_tabla_docentes INT NOT NULL,
    id_tabla_asignaturas INT NOT NULL,
    
    CONSTRAINT pk_docentes_asignaturas PRIMARY KEY (id_docente_asignatura),
    CONSTRAINT fk_tabla_docentes FOREIGN KEY (id_tabla_docentes) REFERENCES docentes (id_docente),
    CONSTRAINT fk_tabla_asignaturas FOREIGN KEY (id_tabla_asignaturas) REFERENCES asignaturas (id_asignatura)
);

CREATE TABLE IF NOT EXISTS opciones_menu(
    id_opcion_menu INT AUTO_INCREMENT,
    opcion_menu VARCHAR(250) NOT NULL,
    numero_opcion INT NOT NULL,
    tipo_menu INT NOT NULL,
    
    CONSTRAINT pk_opciones_menu PRIMARY KEY (id_opcion_menu)
);