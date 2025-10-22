class Cliente:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    def validar_email(self) -> bool:
        '''Valida la estructura de mi correo'''
        return "@" in self.correo and "." in self.correo
    
    def __str__(self):
        return "texto"
    
client = Cliente("Jony", "correo@hotmail.com")

print(client.validar_email())