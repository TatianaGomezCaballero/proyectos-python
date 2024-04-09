# texto ingresado por el usuario
texto = input('Ingresa un texto porfavor: ')
texto_minuscula = texto.lower()
texto_en_lista = list(texto_minuscula)
largo_texto = len(texto_en_lista)

# letras ingresadas por el usurio
letras = input('Por favor ingresa tres letras : ')
letras_minusculas = letras.lower()
letras_en_lista = list(letras_minusculas)

# cuantas veces aparecen esas letras en el texto
numero_de_apariciones1 = texto_en_lista.count(letras_en_lista[0])
print(f'La primera letra aparece {numero_de_apariciones1} veces')

numero_de_apariciones2 = texto_en_lista.count(letras_en_lista[1])
print(f'La primera letra aparece {numero_de_apariciones2} veces')

numero_de_apariciones3 = texto_en_lista.count(letras_en_lista[2])
print(f'La primera letra aparece {numero_de_apariciones3} veces')

# mostrando cuantas letras hay en el texto
print(f'El total de palabras que hay en el texto que escribiste es: {largo_texto}')

# mostrar la primera y ultima letra dell texto
index = texto_en_lista[0]
print('La primera letra es', index)

index2 = texto_en_lista[-1]
print('La ultima letra es', index2)

# texto unido
texto_unido = ' '.join(texto_en_lista)
print(f'El texto unido seria asi: {texto_unido}')

# texto invertido
texto_en_lista.reverse()
print(f'La lista en reversa seria asi: {texto_en_lista}')


# mostrar si esta python en el texto

mi_dict = {'Si se ecuentra la palabra en el texto ': 'True',
           'Si no se ecuentra la palabra en el texto': 'False'}

print(f'Esta es la consigna si se encuentra o no la palabra, {mi_dict}')

is_python = 'python' in texto_en_lista
print(is_python)







