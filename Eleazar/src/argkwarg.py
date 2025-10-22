#args

def procesar_datos(*args) -> None:
    '''Recibe argumentos posicionales'''
    print(f"Argumentos: {args}")

#keyword arguments

def procesar_datos_kwg(**kwargs) -> None:
    '''Recibe argumentos por clave valor'''
    print(f"Argumentos: {kwargs}")

procesar_datos(10, 50, 5, 4, 2)
procesar_datos_kwg(nombre="Jona", status= True)