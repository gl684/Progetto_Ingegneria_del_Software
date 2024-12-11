from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from listaclienti.views.finestralistaclienti import Ui_FinestraListaClienti
from listaclienti.controller.ControlloreListaClienti import ControlloreListaClienti
from cliente.views.VistaCliente import VistaCliente
from listaclienti.views.VistaInserisciCliente import VistaInserisciCliente


class VistaListaClienti(QMainWindow):
    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        # Inizializza l'interfaccia grafica generata
        self.ui = Ui_FinestraListaClienti()
        self.ui.setupUi(self)

        # Inizializza il controller
        self.controller = ControlloreListaClienti()

        # Collega i pulsanti ai metodi
        self.ui.ButtonApriCliente.clicked.connect(self.show_selected_info)
        self.ui.ButtonAggiungiCliente.clicked.connect(self.show_new_cliente)

        # Aggiorna la lista clienti
        self.update_ui()

    def update_ui(self):
        """Aggiorna la lista dei clienti nella QListWidget."""
        self.ui.ListaClienti.clear()
        lista_clienti = self.controller.get_lista_dei_clienti()
        if not lista_clienti:
            self.ui.ListaClienti.addItem("Nessun cliente presente.")  # Messaggio visivo
            return

        for cliente in lista_clienti:
            nome_cliente = (
                f"{cliente.nome} {cliente.cognome}"
                if cliente.is_privato()
                else cliente.nome_azienda
            )
            item = QListWidgetItem(nome_cliente)
            self.ui.ListaClienti.addItem(item)

    def show_selected_info(self):
        """Mostra le informazioni del cliente selezionato."""
        selected_item = self.ui.ListaClienti.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Nessuna selezione", "Seleziona un cliente dalla lista.")
            return

        selected_index = self.ui.ListaClienti.row(selected_item)
        cliente_selezionato = self.controller.get_cliente_by_index(selected_index)

        if not cliente_selezionato:
            QMessageBox.critical(self, "Errore", "Cliente non trovato.")
            return

        # Chiudi eventuali finestre precedenti
        if hasattr(self, 'vista_cliente') and self.vista_cliente is not None:
            self.vista_cliente.close()

        self.vista_cliente = VistaCliente(
            cliente_selezionato,
            self.controller.elimina_cliente_by_id,
            self.update_ui
        )
        self.vista_cliente.show()

    def show_new_cliente(self):
        """Mostra la finestra per inserire un nuovo cliente."""
        try:
            if hasattr(self, 'vista_inserisci_cliente') and self.vista_inserisci_cliente is not None:
                self.vista_inserisci_cliente.close()

            self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
            self.vista_inserisci_cliente.setWindowModality(QtCore.Qt.ApplicationModal)
            self.vista_inserisci_cliente.show()
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore durante l'apertura della finestra: {e}")

    def closeEvent(self, event):
        """Salva i dati alla chiusura della finestra."""
        self.controller.save_data()
        event.accept()
