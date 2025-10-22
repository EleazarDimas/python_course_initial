# #Clase que almacena el pedido
# #class RepositorioBD:
# #    def guardar(self, pedido):
# #       print(f"Pedido {pedido} almacenado exitosamente")

# #Clase que implementa logica de negocio del pedido
# class ServicePedidos:
#     def set_repo(self, repositorio: RepositorioBD):
#         '''Inicializa la instancia del repositorio'''
#         self.repositorio = repositorio

#     def __init__(self, repositorio: RepositorioBD):
#         self.repositorio = repositorio
#     def crear_pedido(self, pedido: str):
#         print("notificacion por mensaje")
#         print("imprimiendo orden")
#         self.repositorio.guardar(pedido)
#         print("Notificacion de almacenado")

# #Inyecci[on de dependencias por constructor]
# repo = RepositorioBD()
# service = ServicePedidos(repo)

# #Llamada al setter
# service.set_repo(repo)

# #Llamada al servicio
# #service.crear_pedido("Hamburguesita")

'''
     Interfaces como patrones
'''

from abc import ABC, abstractmethod

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


# repoDB: IRepositorioDB = RepositorioDB()
# repoApi: IRepositorioDB = ApiTercerosAdapter()
# service = ServicePedido(repoDB)
# servicedos = ServicePedido(repoApi)

# service.crear_pedido("tacos")
# servicedos.crear_pedido("Sincronizadas")
        

class Container:
    def __init__(self):
        self.servicios = {}
    
    def register(self, nombre, creator):
        self._servicios[nombre] = creator

    def resolver(self, nombre):
        return self._servicios[nombre]()
    
container = Container()
container.register("repositorio", lambda: RepositorioDB())
container.register("Service", lambda: ServicePedido(container.resolver("repositorio")))

service = container.resolver("service")
service.crear_pedido("Taquitos")
