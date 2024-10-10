class ControlloreOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def get_nome_ordine(self):
        return self.model.nome_ordine

    def get_oggetto_ordine(self):
        return self.model.oggetto_ordine

    def get_data_inizio(self):
        return self.model.data_inizio

    def get_data_termine(self):
        return self.model.data_termine

    def get_stato(self):
        return self.model.stato

    def get_fasi(self):
        return self.model.list_fasi