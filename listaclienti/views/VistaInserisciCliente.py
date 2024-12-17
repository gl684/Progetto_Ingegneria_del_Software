import re

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from cliente.model.Cliente import Cliente
from listaclienti.views.finestrainseriscicliente import Ui_FinestraInserisciCliente


class VistaInserisciCliente(QMainWindow):
    def __init__(self, controller, callback_update_ui, parent=None):
        super(VistaInserisciCliente, self).__init__(parent)

        #Inizializza il controller
        self.controller = controller

        self.callback_update_ui = callback_update_ui

        #Configura l'interfaccia utente
        self.ui = Ui_FinestraInserisciCliente()
        self.ui.configurazioneInterfaccia(self)

        #Nascondi i campi azienda all'inizio
        self.mostra_campi_specifici()

        #Collega segnali
        self.ui.comboBoxTipoCliente.currentIndexChanged.connect(self.mostra_campi_specifici)
        self.ui.ButtonConferma.clicked.connect(self.aggiungi_cliente)
        self.ui.ButtonAnnulla.clicked.connect(self.close)

        #Collega i segnali textChanged per i campi Codice Fiscale e Partita IVA
        self.ui.lineEditCF.textChanged.connect(self.converti_maiuscolo_cf)
        self.ui.lineEditPartitaIVA.textChanged.connect(self.converti_maiuscolo_piva)

    def mostra_campi_specifici(self):
        """Nasconde o mostra i campi specifici in base al tipo di cliente selezionato."""
        tipo_cliente = self.ui.comboBoxTipoCliente.currentText()

        is_privato = (tipo_cliente == "Privato")

        #Campi specifici per Cliente Privato
        campo_privato = [
            (self.ui.labelNome, self.ui.lineEditNome),
            (self.ui.labelCognome, self.ui.lineEditCognome),
            (self.ui.labelCF, self.ui.lineEditCF),
        ]

        #Campi specifici per Cliente Azienda
        campo_azienda = [
            (self.ui.labelNomeAzienda, self.ui.lineEditNomeAzienda),
            (self.ui.labelPartitaIVA, self.ui.lineEditPartitaIVA),
        ]

        #Mostra/Nascondi campi specifici
        for label, field in campo_privato:
            label.setVisible(is_privato)
            field.setVisible(is_privato)

        for label, field in campo_azienda:
            label.setVisible(not is_privato)
            field.setVisible(not is_privato)

        #Campi comuni sempre visibili
        self.ui.labelIndirizzo.setVisible(True)
        self.ui.lineEditIndirizzo.setVisible(True)
        self.ui.labelTelefono.setVisible(True)
        self.ui.lineEditTelefono.setVisible(True)
        self.ui.labelEmail.setVisible(True)
        self.ui.lineEditEmail.setVisible(True)

    def converti_maiuscolo_cf(self):
        """Converte il testo del campo Codice Fiscale in maiuscolo."""
        text = self.ui.lineEditCF.text()
        self.ui.lineEditCF.setText(text.upper())

    def converti_maiuscolo_piva(self):
        """Converte il testo del campo Partita IVA in maiuscolo."""
        text = self.ui.lineEditPartitaIVA.text()
        self.ui.lineEditPartitaIVA.setText(text.upper())

    def aggiungi_cliente(self):
        """Aggiunge un cliente alla lista."""
        tipo_cliente = self.ui.comboBoxTipoCliente.currentText()

        #Raccogli i dati dai campi comuni
        cliente_data = {
            "email": self.ui.lineEditEmail.text().strip(),
            "telefono": self.ui.lineEditTelefono.text().strip(),
            "indirizzo": self.ui.lineEditIndirizzo.text().strip(),
            "tipo_cliente": tipo_cliente  # Passa il tipo di cliente
        }

        #Aggiunta dei campi specifici
        if tipo_cliente == "Privato":
            cliente_data.update({
                "nome": self.ui.lineEditNome.text().strip(),
                "cognome": self.ui.lineEditCognome.text().strip(),
                "cf": self.ui.lineEditCF.text().strip(),
            })
        elif tipo_cliente == "Azienda":
            cliente_data.update({
                "nome_azienda": self.ui.lineEditNomeAzienda.text().strip(),
                "partita_iva": self.ui.lineEditPartitaIVA.text().strip(),
            })

        #Verifica se tutti i campi richiesti sono compilati
        valid, error_message = self.valida_campi_nuovo_cliente(cliente_data, tipo_cliente)
        if not valid:
            QMessageBox.critical(self, "Errore", error_message, QMessageBox.Ok)
            return

        #Aggiunta del cliente al controller
        try:
            cliente = Cliente(**cliente_data)  # Passa tutti i dati al costruttore di Cliente
            self.controller.aggiungi_cliente(cliente)
            QMessageBox.information(self, "Successo", "Cliente aggiunto correttamente!", QMessageBox.Ok)
            self.callback_update_ui()  # Aggiorna l'interfaccia utente chiamante
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore durante l'aggiunta: {e}", QMessageBox.Ok)

    def verifica_email_valida(self, email):
        """Verifica se l'email è in un formato valido."""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def valida_campi_nuovo_cliente(self, cliente_data, tipo_cliente):
        """Valida i campi richiesti per il cliente specificato."""
        if tipo_cliente == "Privato":
            campi_richiesti = ["nome", "cognome", "cf", "email", "telefono", "indirizzo"]
        elif tipo_cliente == "Azienda":
            campi_richiesti = ["nome_azienda", "partita_iva", "email", "telefono", "indirizzo"]
        else:
            return False, "Tipo cliente non valido."

        #Controlla se tutti i campi richiesti sono compilati
        for field in campi_richiesti:
            if not cliente_data.get(field):
                return False, "Dati mancanti. Compila tutti i campi richiesti."

        #Validazione email
        if not self.verifica_email_valida(cliente_data["email"]):
            return False, "L'email fornita non è valida."

        return True, ""




