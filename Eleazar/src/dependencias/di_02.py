from abc import ABC, abstractmethod
from dependency_injector import containers, providers

class IRepositorioDB(ABC):
     @abstractmethod
     def guardar(self, pedido):
         pass

class ApiTercerosAdapter(IRepositorioDB):
     def guardar(self, pedido):
         print(f"Guardado de manera distinta {pedido}")

class RepositorioDB(IRepositorioDB):
     def guardar(self, pedido):
         print(f"pedido {pedido} almacenado exitosamente")

class ServicePedido:
     def __init__(self, repositorio: IRepositorioDB):
         self.repo = repositorio

     def crear_pedido(self, pedido: str):
         print("notificacion por mensaje")
         print("imprimiendo orden")
         self.repo.guardar(pedido)
         print("Notificacion de almacenado")

#Dependency injector with pip package
class Contenedor(containers.DeclarativeContainer):
    repositorio = providers.Singleton(RepositorioDB)
    service = providers.Factory(ServicePedido, repositorio = repositorio)

container = Contenedor()
service_instance = container.service()
service_instance_two = container.service()

service_instance.crear_pedido("Pan de muerto")
service_instance_two.crear_pedido("Pan de muerto")

print(service_instance_two is service_instance)
