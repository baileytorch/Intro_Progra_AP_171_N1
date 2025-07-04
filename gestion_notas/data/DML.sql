INSERT INTO docentes (rut_docente,digito_ver,nombre_docente) VALUES
(12345678,'5','Aquiles Brinco'),
(12345679,'k','Alan Brito Delgado');

INSERT INTO asignaturas (codigo_asig,nombre_asig) VALUES
('BIO','Biología Celular'),
('QUI','Química Inorgánica');

INSERT INTO opciones_menu (opcion_menu,numero_opcion,tipo_menu) VALUES
('Gestión Asignaturas',1,1),
('Gestión Docentes',2,1),
('salir',0,1),
('Listado Asignaturas',1,2),
('Agregar Asignatura',2,2),
('Editar Asignatura',3,2),
('Eliminar Asignatura',4,2),
('salir',0,2),
('Listado Docentes',1,3),
('Agregar Docente',2,3),
('Editar Docente',3,3),
('Eliminar Docente',4,3),
('salir',0,3);