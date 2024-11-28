from PyQt5 import QtCore
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
        self.ui.ButtonListaClienti.clicked.connect(self.go_lista_clienti)
        self.ui.ButtonListaOrdini.clicked.connect(self.go_lista_ordini)
        self.ui.ButtonListaDipendenti.clicked.connect(self.go_lista_dipendenti)
        self.ui.ButtonListaDocumenti.clicked.connect(self.go_lista_documenti)
        self.ui.ButtonListaFornitori.clicked.connect(self.go_lista_fornitori)
        self.ui.ButtonListaEntiEsterni.clicked.connect(self.go_lista_enti_esterni)
        self.ui.ButtonListaProdotti.clicked.connect(self.go_lista_prodotti)
        self.ui.ButtonListaMacchine.clicked.connect(self.go_lista_macchine)

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.setWindowModality(QtCore.Qt.ApplicationModal)
        self.vista_lista_clienti.show()

    def go_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.setWindowModality(QtCore.Qt.ApplicationModal)
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
