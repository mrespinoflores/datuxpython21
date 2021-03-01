n = int(input('¿Cuántos números desea introducir? '))

if n > 8:
    print('No se puede procesar el dato, ingrese otro número.')
elif n < 1:
    print('No se puede procesar el dato, ingrese otro número.')
else:
    for i in range(1,n+1):
        print(" " * (n-i) + '#'*i)