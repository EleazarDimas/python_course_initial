# Comentario bonito

"""
usando un comentario multi linea 
"""

variable_numero = 3
variable_bool = False

print(type(variable_numero))

variable_numero = "Hola"

print(type(variable_numero))

a, b, c = 1, 2, 3

print(a + b)

a = b = c = 2 
print(a * b * c)

#Compresiones
#lista de números
numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0  ]
print(pares)