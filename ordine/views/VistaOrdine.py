from PyQt5 import QtWidgets
from ordine.views.finestravisualizzaordine import Ui_FinestraVisualizzaOrdine
from ordine.controller.ControlloreOrdine import ControlloreOrdine

class VistaOrdine(QtWidgets.QMainWindow):
    def __init__(self, ordine):
        super().__init__()

        print(f"Costruzione di VistaOrdine per: {ordine.nome_ordine}")  # Debug

        #Controller per l'ordine
        self.controller = ControlloreOrdine(ordine)

        #Verifica i dati del controller
        print(f"Nome ordine: {self.controller.get_nome_ordine()}")
        print(f"Fasi dell'ordine: {self.controller.get_fasi()}")

        # Setup interfaccia grafica
        self.ui = Ui_FinestraVisualizzaOrdine()
        self.ui.configurazioneInterfaccia(self)

        #Popola i dati generali dell'ordine
        self.ui.labelNomeOrdine.setText(f"Nome Ordine: {self.controller.get_nome_ordine()}")
        self.ui.labelOggettoOrdine.setText(f"Oggetto Ordine: {self.controller.get_oggetto_ordine()}")
        self.ui.labelDataInizio.setText(f"Data Inizio: {self.controller.get_data_inizio()}")
        self.ui.labelDataTermine.setText(f"Data Termine: {self.controller.get_data_termine()}")
        self.ui.labelStatoOrdine.setText(f"Stato: {self.controller.get_stato()}")
        self.ui.labelIDOrdine.setText(f"ID Ordine: {self.controller.get_id_ordine()}")

        #Popola la tabella delle fasi
        self.popola_tabella()

    def popola_tabella(self):
        """Popola la tabella delle fasi."""
        fasi = self.controller.get_fasi()
        print(f"Fasi ricevute: {fasi}")  # Debug: stampare le fasi ricevute
        self.ui.TabellaFasiOrdine.setRowCount(len(fasi))
        self.ui.TabellaFasiOrdine.setColumnCount(4)
        self.ui.TabellaFasiOrdine.setHorizontalHeaderLabels(["Numero", "Nome Fase", "Stato", "Esternalizzazione"])

        for row, fase in enumerate(fasi):
            print(f"Popolamento riga {row}: {fase}")  # Debug: stampare i dati della fase
            self.ui.TabellaFasiOrdine.setItem(row, 0, QtWidgets.QTableWidgetItem(str(fase.numero_fase)))
            self.ui.TabellaFasiOrdine.setItem(row, 1, QtWidgets.QTableWidgetItem(fase.nome_fase))
            self.ui.TabellaFasiOrdine.setItem(row, 2, QtWidgets.QTableWidgetItem(fase.stato_fase))
            self.ui.TabellaFasiOrdine.setItem(row, 3,
                                              QtWidgets.QTableWidgetItem("Sì" if fase.esternalizzazione_fase else "No"))
