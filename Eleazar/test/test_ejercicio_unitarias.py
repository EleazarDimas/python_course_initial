from src.dependencias.di_02 import ServicePedido, RepositorioDB, IRepositorioDB

class TestServicePedido():
    def test_crear_pedido_con_repositorio_terceros(self):
        repo: IRepositorioDB = RepositorioDB()
        service = ServicePedido(repo)
        service.crear_pedido("pedido_2")



