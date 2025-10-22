import time

#utilidad de time
print("Time", time.time())
sum([i**2 for i in range(10000)])
print("Time", time.time())

def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("Final")
    return envoltura


@decorador
def saludo():
    #print("Inicio")
    print("Hola mundo")
    #print("Final")


saludo()

funcion_decorada = decorador(saludo)
funcion_decorada()