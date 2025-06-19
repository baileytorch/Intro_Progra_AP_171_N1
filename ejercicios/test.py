while True:
    try:
        numerador = int(input('Ingrese el numerador: '))
        denominador = int(input('Ingrese el denominador: '))

        division = numerador/denominador
        print(f'{numerador}/{denominador}= {division}')

        respuesta = input('Desea continuar Si, No...')
        if respuesta.lower() == 'no':
            break
    except:
        print('Numero no corresponde a entero...')