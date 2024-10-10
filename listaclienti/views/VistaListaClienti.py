from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from cliente.views.VistaCliente import VistaCliente
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente


class VistaListaClienti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        self.controller = ControlloreListaClienti()

        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton("Nuovo")
        new_button.clicked.connect(self.show_new_cliente)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle("Lista Clienti")

    def show_selected_info(self):
        # Controlliamo che ci sia un elemento selezionato
        selected_indexes = self.list_view.selectedIndexes()
        if not selected_indexes:
            return  # Se non c'è alcun elemento selezionato, non fare nulla

        # Prendiamo l'indice selezionato
        selected = selected_indexes[0].row()

        # Recuperiamo il cliente selezionato
        cliente_selezionato = self.controller.get_cliente_by_index(selected)

        # Apriamo la finestra con i dettagli del cliente selezionato
        self.vista_cliente = VistaCliente(
            cliente_selezionato,
            self.controller.elimina_cliente_by_id,
            self.update_ui
        )

        # Separiamo la finestra cliente dal genitore (la finestra principale rimane indipendente)
        self.vista_cliente.setParent(None)

        # Mostriamo la finestra del cliente selezionato
        self.vista_cliente.show()

    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()

    def update_ui(self):
        print("Aggiornamento lista clienti...")
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_dei_clienti():
            print(
                f"Aggiungendo cliente: {cliente.nome} {cliente.cognome if cliente.is_privato() else cliente.nome_azienda}")
            item = QStandardItem()
            if cliente.is_privato():
                item.setText(cliente.nome + " " + cliente.cognome)
            else:
                item.setText(cliente.nome_azienda)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
        print("VistaListaClienti chiusa")  # Log di chiusura
        event.accept()  # Permetti la chiusura della finestra