from version.version import versionamiento

def programa_principal():
    version = versionamiento()
    while True:
        print(f"*** Manejo Inventario {version} ***")
        break

programa_principal()