from dataclasses import dataclass

@dataclass
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

## dataclass

@dataclass
class PersonaDto:
    nombre: str
    edad: int
    cat: str
person = PersonaDto("Jon", 25, "Dev")

print(person)