def fibonacci_gen(limit: int):
    '''Ejercicio fibonacci'''
    print("Inicio del generador")
    a, b = 0, 1
    for i in range(limit):
        yield a
        c = b
        b = a + b
        a = c
    print("Fin del generador")




for numero in fibonacci_gen(10):
  print("En generador", numero)