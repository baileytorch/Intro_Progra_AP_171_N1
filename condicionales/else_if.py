""" 
Clase AB: $7,177,530.
Clase C1a: $3,010,391.
Clase 1B: $2,072,853 .
Clase C2: $1,500,774.
Clase C3: $1,003,426.
Clase D: $640,667.
Clase E: $361,583. 
"""
print("Ingrese su sueldo:")
sueldo = input()
sueldo_int = int(sueldo)

if sueldo_int > 3010391 :
    print("Ud. pertenece a la clase AB")
elif sueldo_int > 2072853:
    print("Ud. pertenece a la clase C1a")
else:
    print("Ud. es muy pobre")