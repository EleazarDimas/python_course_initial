def saludar(nombre: str) -> str:
    """función que devuelve un saludo"""
    return f"Hola {nombre}"

print(saludar(3))

def saludo_generico(nombre = 'Usuario'):
    return f"Hola {nombre}"

print(saludo_generico("Juanito"))

#Funcion con argumento kwargs

#lambda 

def suma(num1: int, num2: int) -> int:
    """suma de 2 enteros"""
    return num1 + num2

suma_lambda = lambda n1, n2 : n1 + n2

print(suma(2, 3))

print(suma_lambda(2, 3))

#Map y filter

#Map

'''
    Un map nos modifica cada elemento de mi lista
    Un filter nos selecciona cada elemento de mi lista
'''
lista_numeros = [1,2,3,4,5]

print("Antes de map y filter")
print(lista_numeros)



tipo_dato = type(map(lambda x: x**2, lista_numeros))

print(tipo_dato)

cuadrados = list(map(lambda x: x**2, lista_numeros))

print(cuadrados)

#filter

pares = list(filter(lambda x: x%2 == 0, lista_numeros))

print(pares)

print("despues de map y filter")
print(lista_numeros)


