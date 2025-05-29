asignaturas = ['Biología','Química','Física']

def obtener_listado_asignaturas():    
    print()
    print('Listado de Asignaturas')
    print('======================')
    contador = 0
    for asignatura in sorted(asignaturas):
        contador += 1
        print(f'[{contador}] {asignatura}')

def obtener_asignatura_individual():
    busqueda = input("Ingrese Asignarura a buscar: ")
    busqueda = input("Ingrese Asignarura a")