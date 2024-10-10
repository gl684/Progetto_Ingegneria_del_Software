from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QMessageBox

from listaclienti.views.VistaListaClienti import VistaListaClienti
from listaordini.views.VistaListaOrdini import VistaListaOrdini


class VistaHome(QWidget):

    # andiamo a definire il costruttore
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Ordini", self.go_lista_ordini), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Documenti", self.go_lista_documenti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Fornitori", self.go_lista_fornitori), 2, 0)
        grid_layout.addWidget(self.get_generic_button("Lista EntiEsterni", self.go_lista_enti_esterni), 2, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Prodotti", self.go_lista_prodotti), 3, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Macchine", self.go_lista_macchine), 3, 1)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore Tipografia")

        # Funzione per creare pulsanti generici
    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # Collega il signal click del pulsante alla funzione on_click
        button.clicked.connect(on_click)
        # restituisci il bottone
        return button

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()

    def go_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.show()

    def go_lista_dipendenti(self):
        QMessageBox.information(self, "Lista Dipendenti", "Funzionalità non ancora implementata")

    def go_lista_documenti(self):
        QMessageBox.information(self, "Lista Documenti", "Funzionalità non ancora implementata")

    def go_lista_fornitori(self):
        QMessageBox.information(self, "Lista Fornitori", "Funzionalità non ancora implementata")

    def go_lista_enti_esterni(self):
        QMessageBox.information(self, "Lista EntiEsterni", "Funzionalità non ancora implementata")

    def go_lista_prodotti(self):
        QMessageBox.information(self, "Lista Prodotti", "Funzionalità non ancora implementata")

    def go_lista_macchine(self):
        QMessageBox.information(self, "Lista Macchine", "Funzionalità non ancora implementata")
