from PyQt5.QtWidgets import QMainWindow, QMessageBox
from home.views.finestrahome import Ui_FinestraHome
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listaordini.views.VistaListaOrdini import VistaListaOrdini



class VistaHome(QMainWindow):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        self.ui = Ui_FinestraHome()  # Crea un'istanza della UI generata
        self.ui.setupUi(self)  # Configura la UI nella finestra corrente

        # Collega i pulsanti alle funzioni esistenti
        self.ui.button_lista_clienti.clicked.connect(self.go_lista_clienti)
        self.ui.button_lista_ordini.clicked.connect(self.go_lista_ordini)
        self.ui.button_lista_dipendenti.clicked.connect(self.go_lista_dipendenti)
        self.ui.button_lista_documenti.clicked.connect(self.go_lista_documenti)
        self.ui.button_lista_fornitori.clicked.connect(self.go_lista_fornitori)
        self.ui.button_lista_enti_esterni.clicked.connect(self.go_lista_enti_esterni)
        self.ui.button_lista_prodotti.clicked.connect(self.go_lista_prodotti)
        self.ui.button_lista_macchine.clicked.connect(self.go_lista_macchine)

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.show()

    def go_lista_dipendenti(self):
        QMessageBox.information(self, "Dipendenti", "Funzionalità non ancora implementata")

    def go_lista_documenti(self):
        QMessageBox.information(self, "Documenti", "Funzionalità non ancora implementata")

    def go_lista_fornitori(self):
        QMessageBox.information(self, "Fornitori", "Funzionalità non ancora implementata")

    def go_lista_enti_esterni(self):
        QMessageBox.information(self, "EntiEsterni", "Funzionalità non ancora implementata")

    def go_lista_prodotti(self):
        QMessageBox.information(self, "Prodotti", "Funzionalità non ancora implementata")

    def go_lista_macchine(self):
        QMessageBox.information(self, "Macchine", "Funzionalità non ancora implementata")
