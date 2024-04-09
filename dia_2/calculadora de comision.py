nombre = input('Porfavor dime tu nombre: ')
ventas = input('cuanto has vendido este mes: ')
conversion = int(ventas)

comision = conversion * 0.13
redondeo = round(comision, 2)

print(f'Hola {nombre}, este mes te ganaste de comision {redondeo} pesos, sigue asi' )
