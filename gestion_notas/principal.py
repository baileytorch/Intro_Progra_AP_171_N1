from negocio.negocio_asignaturas import obtener_listado_asignaturas,guardar_nueva_asignatura

def menu_principal():
    print()
    print("Sistema Gestión Notas")
    print("=====================")
    print("[1] Gestión de Asignaturas")
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
                pass
            elif opcion_submenu_asignaturas == "4":
                pass
            elif opcion_submenu_asignaturas == "0":
                pass
            else:
                print("Opción Inválida, vuelva a ingresar...")
                return
        elif opcion_menu == "0":
            break
        else:
            print("Opción Inválida, vuelva a ingresar...")

ejecucion_principal()