deposito = float(input('Ingrese cantidad de dinero depositada en su nueva cuenta de ahorros: S/ '))

año1=deposito+(deposito*0.04)

print('Tras el primer año, usted habrá acumulado: S/ {}'.format(round(año1,2)))
año2=año1+(año1*0.04)
print('Tras el segundo año, usted habrá acumulado: S/ {}'.format(round(año2,2)))
año3=año2+(año2*0.04)
print('Tras el tercer año, usted habrá acumulado: S/ {}'.format(round(año3,2)))