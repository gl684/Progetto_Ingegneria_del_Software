from listaclienti.model.ListaClienti import ListaClienti


class ControlloreListaClienti():
    def __init__(self):
        super(ControlloreListaClienti, self).__init__()
        self.model = ListaClienti()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def get_lista_dei_clienti(self):
        lista_clienti = self.model.get_lista_clienti()
        print(f"Lista clienti ottenuta dal modello: {lista_clienti}")
        return lista_clienti

    def get_cliente_da_indice(self, index):
        return self.model.get_cliente_da_indice(index)

    def elimina_cliente_da_id(self, id):
        self.model.rimuovi_cliente_da_id(id)

    def salva_dati(self):
        self.model.salva_dati()
