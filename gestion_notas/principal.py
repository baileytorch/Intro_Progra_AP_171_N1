from negocio.negocio_asignaturas import obtener_listado_asignaturas,guardar_nueva_asignatura,actualizar_asignatura,eliminar_asignatura
from negocio.negocio_docentes import obtener_listado_docentes, guardar_nuevo_docente,actualizar_docente,eliminar_docente

def menu_principal():
    print()
    print("Sistema Gestión Notas")
    print("=====================")
    print("[1] Gestión de Asignaturas")
    print("[2] Gestión de Docentes")
    print("[0] Salir")
    print()

def sub_menu_asignaturas():
    print()
    print("Gestión Asignaturas")
    print("===================")
    print("[1] Listado de Asignaturas")
    print("[2] Agregar Asignatura")
    print("[3] Modificar Asignatura")
    print("[4] Eliminar Asignatura")
    print("[0] Volver al menú principal")
    print()

def sub_menu_docentes():
    print()
    print("Gestión Docentes")
    print("================")
    print("[1] Listado de Docentes")
    print("[2] Agregar Docente")
    print("[3] Modificar Docente")
    print("[4] Eliminar Docente")
    print("[0] Volver al menú principal")
    print()

def ejecucion_principal():
    while True:
        menu_principal()
        opcion_menu = input("Seleccione su Opción [0-1]: ")
        
        if opcion_menu == "1":
            sub_menu_asignaturas()
            opcion_submenu_asignaturas = input("Seleccione su Opción [0-4]: ")
            
            if opcion_submenu_asignaturas == "1":
                obtener_listado_asignaturas()
            elif opcion_submenu_asignaturas == "2":
                guardar_nueva_asignatura()
            elif opcion_submenu_asignaturas == "3":
                actualizar_asignatura()
            elif opcion_submenu_asignaturas == "4":
                eliminar_asignatura()
            elif opcion_submenu_asignaturas == "0":
                pass
            else:
                print("Opción Inválida, vuelva a ingresar...")
                return
        elif opcion_menu == "2":
            sub_menu_docentes()
            opcion_submenu_docentes = input("Seleccione su Opción [0-4]: ")

            if opcion_submenu_docentes == "1":
                obtener_listado_docentes()
            elif opcion_submenu_docentes == "2":
                guardar_nuevo_docente()
            elif opcion_submenu_docentes == "3":
                actualizar_docente()
            elif opcion_submenu_docentes == "4":
                eliminar_docente()
            elif opcion_submenu_docentes == "0":
                pass
            else:
                print("Opción Inválida, vuelva a ingresar...")
                return
        elif opcion_menu == "0":
            break
        else:
            print("Opción Inválida, vuelva a ingresar...")

ejecucion_principal()