from negocio.negocio_asignaturas import obtener_listado_asignaturas, guardar_nueva_asignatura, actualizar_asignatura, eliminar_asignatura
from negocio.negocio_docentes import obtener_listado_docentes, guardar_nuevo_docente, actualizar_docente, eliminar_docente
from auxiliares.version import version_actual
from data.conexion import leer_datos
import auxiliares.mensajes_sistema as mensajes
from prettytable import PrettyTable


def cargar_menu(tipo_menu, titulo_menu):
    print()
    print(f"Sistema Gestión Notas v.{version_actual}")
    print("==============================")
    consulta = f'''
        SELECT numero_opcion,opcion_menu FROM opciones_menu
        WHERE tipo_menu = {tipo_menu}
    '''
    resultado = leer_datos(consulta)
    tabla_menu = PrettyTable()
    tabla_menu.field_names = ['N°', f'{titulo_menu}']
    contador = 0
    if resultado != None:
        for asignatura in resultado:
            contador += 1
            tabla_menu.add_row(asignatura)  # type: ignore
    print(tabla_menu)
    opcion_menu = input(f"Seleccione su Opción [0-{contador-1}]: ")
    return opcion_menu


def ejecucion_principal():
    while True:
        opcion_menu = cargar_menu(1, 'Menú Principal')

        if opcion_menu == "1":
            while True:
                opcion_submenu = cargar_menu(2, 'Gestión Asignaturas')
                if opcion_submenu == "1":
                    obtener_listado_asignaturas()
                elif opcion_submenu == "2":
                    guardar_nueva_asignatura()
                elif opcion_submenu == "3":
                    actualizar_asignatura()
                elif opcion_submenu == "4":
                    eliminar_asignatura()
                elif opcion_submenu == "0":
                    print(f'{mensajes.volver}')
                    break
                else:
                    print(f'{mensajes.invalido}')

        elif opcion_menu == "2":
            while True:
                opcion_submenu = cargar_menu(3, 'Gestión Docentes')
                if opcion_submenu == "1":
                    obtener_listado_docentes()
                elif opcion_submenu == "2":
                    guardar_nuevo_docente()
                elif opcion_submenu == "3":
                    actualizar_docente()
                elif opcion_submenu == "4":
                    eliminar_docente()
                elif opcion_submenu == "0":
                    print(f'{mensajes.volver}')
                    break
                else:
                    print(f'{mensajes.invalido}')

        elif opcion_menu == "0":
            print(f'{mensajes.salir}')
            break
        else:
            print(f'{mensajes.invalido}')


ejecucion_principal()
