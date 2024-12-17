from listaordini.model.ListaOrdini import ListaOrdini


class ControlloreListaOrdini:
    def __init__(self):
        super(ControlloreListaOrdini, self).__init__()
        self.model = ListaOrdini()

    def get_lista_degli_ordini(self):
        return self.model.get_lista_ordini()

    def get_ordine_da_indice(self, index):
        return self.model.get_ordine_da_indice(index)

    def get_lista_degli_ordini_filtrata(self, tipo_ordine):
        return self.model.get_lista_ordini_filtrata(tipo_ordine)

    def salva_dati(self):
        self.model.salva_dati()  # Salva i dati quando necessario
