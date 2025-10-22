cons_iva = 1.16

def precio_final(precio_base: int) -> int:
    """se agrega el iva"""
    return precio_base * cons_iva

iva_lambda = lambda n1 : n1 * cons_iva

print("calculo por def")
print(precio_final(50))

print("calculo por lambda")
print(iva_lambda(50))


