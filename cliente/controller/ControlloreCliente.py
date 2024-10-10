from listaclienti.model.ListaClienti import ListaClienti


class ClienteController:
    def __init__(self):
        self.lista_clienti = ListaClienti()

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.aggiungi_cliente(cliente)

    def elimina_cliente(self, cliente_id):
        self.lista_clienti.elimina_cliente(cliente_id)

    def modifica_cliente(self, cliente_modificato):
        self.lista_clienti.modifica_cliente(cliente_modificato)
