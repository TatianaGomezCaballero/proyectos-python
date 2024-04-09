lista_precios = [('moka', 1200), ('capuccino', 1456), ('expresso', 1100)]

def cafe_mas_caro(lista_precios):
    precio_mahyor = 0
    cafe_mas_costoso = ''

    for cafe,precio in lista_precios:
        if precio > precio_mahyor:
            precio_mahyor = precio
            cafe_mas_costoso = cafe
        else:
            pass

    return (precio_mahyor, cafe_mas_costoso)

resultado = cafe_mas_caro(lista_precios)
print(resultado)