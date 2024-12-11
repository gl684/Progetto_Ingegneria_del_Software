import re

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from cliente.model.Cliente import Cliente
from listaclienti.views.finestrainseriscicliente import Ui_FinestraInserisciCliente


class VistaInserisciCliente(QMainWindow):
    def __init__(self, controller, callback_update_ui, parent=None):
        super(VistaInserisciCliente, self).__init__(parent)

        # Inizializza il controller
        self.controller = controller

        self.callback_update_ui = callback_update_ui

        # Configura l'interfaccia utente
        self.ui = Ui_FinestraInserisciCliente()
        self.ui.setupUi(self)

        # Nascondi i campi azienda all'inizio
        self.toggle_fields()

        # Collega segnali
        self.ui.comboBox_tipo_cliente.currentIndexChanged.connect(self.toggle_fields)
        self.ui.ButtonConferma.clicked.connect(self.aggiungi_cliente)
        self.ui.ButtonAnnulla.clicked.connect(self.close)

    def toggle_fields(self):
        """Nasconde o mostra i campi specifici in base al tipo di cliente selezionato."""
        tipo_cliente = self.ui.comboBox_tipo_cliente.currentText()

        is_privato = (tipo_cliente == "Privato")

        # Campi specifici per Cliente Privato
        privato_fields = [
            (self.ui.label_nome, self.ui.lineEdit_nome),
            (self.ui.label_cognome, self.ui.lineEdit_cognome),
            (self.ui.label_codice_fiscale, self.ui.lineEdit_codice_fiscale),
        ]

        # Campi specifici per Cliente Azienda
        azienda_fields = [
            (self.ui.label_nome_azienda, self.ui.lineEdit_nome_azienda),
            (self.ui.label_partita_iva, self.ui.lineEdit_partita_iva),
        ]

        # Mostra/Nascondi campi specifici
        for label, field in privato_fields:
            label.setVisible(is_privato)
            field.setVisible(is_privato)

        for label, field in azienda_fields:
            label.setVisible(not is_privato)
            field.setVisible(not is_privato)

        # Campi comuni sempre visibili
        self.ui.label_indirizzo.setVisible(True)
        self.ui.lineEdit_indirizzo.setVisible(True)
        self.ui.label_telefono.setVisible(True)
        self.ui.lineEdit_telefono.setVisible(True)
        self.ui.label_email.setVisible(True)
        self.ui.lineEdit_email.setVisible(True)

    def aggiungi_cliente(self):
        """Aggiunge un cliente alla lista."""
        tipo_cliente = self.ui.comboBox_tipo_cliente.currentText()

        # Raccogli i dati dai campi comuni
        cliente_data = {
            "email": self.ui.lineEdit_email.text().strip(),
            "telefono": self.ui.lineEdit_telefono.text().strip(),
            "indirizzo": self.ui.lineEdit_indirizzo.text().strip(),
        }

        # Aggiunta dei campi specifici
        if tipo_cliente == "Privato":
            cliente_data.update({
                "nome": self.ui.lineEdit_nome.text().strip(),
                "cognome": self.ui.lineEdit_cognome.text().strip(),
                "cf": self.ui.lineEdit_codice_fiscale.text().strip(),
            })
        elif tipo_cliente == "Azienda":
            cliente_data.update({
                "nome_azienda": self.ui.lineEdit_nome_azienda.text().strip(),
                "partita_iva": self.ui.lineEdit_partita_iva.text().strip(),
            })

        # Verifica se tutti i campi richiesti sono compilati
        valid, error_message = self.validate_fields(cliente_data, tipo_cliente)
        if not valid:
            QMessageBox.critical(self, "Errore", "Dati mancanti. Compila tutti i campi richiesti.", QMessageBox.Ok)
            return

        # Aggiunta del cliente al controller
        try:
            cliente = Cliente(**cliente_data)
            self.controller.aggiungi_cliente(cliente)
            QMessageBox.information(self, "Successo", "Cliente aggiunto correttamente!", QMessageBox.Ok)
            self.callback_update_ui()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore durante l'aggiunta: {e}", QMessageBox.Ok)

    def is_valid_email(self, email):
        """Verifica se l'email è in un formato valido."""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def validate_fields(self, cliente_data, tipo_cliente):
        """Valida i campi richiesti per il cliente specificato."""
        if tipo_cliente == "Privato":
            required_fields = ["nome", "cognome", "cf", "email", "telefono", "indirizzo"]
        else:
            required_fields = ["nome_azienda", "partita_iva", "email", "telefono", "indirizzo"]

        for field in required_fields:
            if not cliente_data.get(field):
                return False, f"Il campo '{field}' è obbligatorio."

        return True, ""



