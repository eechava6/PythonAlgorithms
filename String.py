jmp = ''' string con saltos\n los'''


lenguaje = "Python 3"
semillero = "Big Data"

#Concatenar strings

mensaje = "Aprendiendo " + lenguaje + " en " + semillero
print(mensaje)


mensaje = "Aprendiendo %s en %s" %(lenguaje,semillero)
print(mensaje)

mensaje = "Aprendiendo {} en {}".format(lenguaje,semillero)
print(mensaje)

mensaje = 'Aprendiendo {b} en {a}'.format(a=lenguaje,b=semillero)
print(mensaje)


string_uno = "Python 3 no es compatible con Python 2.x"

print(string_uno)
print(string_uno[0:10]) # Substring
print(string_uno[0:10:2]) # Substring con salto de 2
print(string_uno[::-1]) # Substring con salto de 2


palindromo = "anita lava la tina"

posicion = palindromo.find("la")
print(posicion)

posicion = palindromo.count("l")
print(posicion)

posicion = palindromo.replace("l","f")
print(posicion)

arreglo = palindromo.split(' ')
print(arreglo)


# La mas sencilla e intuitiva
matriz = []
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(None)


# Menos intuitiva pero mas eficiente
matriz = [None] * numero_filas
for i in range(numero_filas):
    matriz[i] = [None] * numero_columnas


matriz = [[0,0,0],[0,0,0],[0,0,0]]