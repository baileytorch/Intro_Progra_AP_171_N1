
# $ 908.469,01	    $ 2.018.820,00	2,20%
# $ 2.018.820,01	$ 3.364.700,00	4,52%
# $ 3.364.700,01	$ 4.710.580,00	7,09%
# $ 4.710.580,01	$ 6.056.460,00	10,62%
# $ 6.056.460,01	$ 8.075.280,00	15,57%
# $ 8.075.280,01	Y MÁS	27,48%

# Pida al usuario que ingrese su sueldo y 
# defina el monto de impuesto de segunda categoría que debe pagar a SII

def definir_impuesto(sueldo):
    sueldo_int = int(sueldo)
    impuesto = 0
    
    if sueldo_int >= 8075280:
        impuesto = ((sueldo_int * 27.48)/100)
    elif sueldo_int >= 6056460 and sueldo_int < 8075280:
        impuesto = ((sueldo_int * 15.57)/100)
    elif sueldo_int >= 4710580 and sueldo_int < 6056460:
        impuesto = ((sueldo_int * 10.62)/100)
    elif sueldo_int >= 3364700 and sueldo_int < 4710580:
        impuesto = ((sueldo_int * 7.09)/100)
    elif sueldo_int >= 2018820 and sueldo_int < 3364700:
        impuesto = ((sueldo_int * 4.52)/100)
    elif sueldo_int >= 908469 and sueldo_int < 2018820:
        impuesto = ((sueldo_int * 2.2)/100)
    else:
        impuesto = 0
    print(f"El impuesto de segunda categoría a pagar con el sueldo de {sueldo_int} es: ${impuesto}")

sueldo_ingresado = input("Ingrese su sueldo: ")
definir_impuesto(sueldo_ingresado)
