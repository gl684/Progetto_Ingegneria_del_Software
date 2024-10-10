from listaordini.model.ListaOrdini import ListaOrdini


class ControlloreListaOrdini:
    def __init__(self):
        super(ControlloreListaOrdini, self).__init__()
        # il suo attributo è il modello perche deve gestire il modello
        self.model = ListaOrdini()

    def get_lista_degli_ordini(self): #ho aggiunto return
        return self.model.get_lista_ordini()

    def get_ordine_by_index(self, index):
        return self.model.get_ordine_by_index(index)

    def get_lista_degli_ordini_filtrata(self, tipo_ordine):
        return self.model.get_lista_ordini_filtrata(tipo_ordine)

    def save_data(self):
        self.model.save_data()  # Salva i dati quando necessario
