from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cliente.views.finestramodificacliente import Ui_FinestraModificaCliente
import re


class VistaModificaCliente(QtWidgets.QMainWindow):
    def __init__(self, cliente, callback_aggiorna_lista, callback_aggiorna_dettagli, parent=None):
        super(VistaModificaCliente, self).__init__(parent)

        self.cliente = cliente
        self.callback_aggiorna_lista = callback_aggiorna_lista
        self.callback_aggiorna_dettagli = callback_aggiorna_dettagli

        #Verifica input obbligatori
        if not self.cliente:
            raise ValueError("L'oggetto cliente non può essere None.")
        if not callable(self.callback_aggiorna_lista):
            raise ValueError("callback_aggiorna_lista deve essere una funzione callable.")
        if not callable(self.callback_aggiorna_dettagli):
            raise ValueError("callback_aggiorna_dettagli deve essere una funzione callable.")

        #Configura l'interfaccia grafica
        self.ui = Ui_FinestraModificaCliente()
        self.ui.configurazioneInterfaccia(self)

        #Configura i campi cliente
        self.configura_cliente()

        #Collega i pulsanti alle funzioni
        self.ui.ButtonSalvaModifica.clicked.connect(self.salva_modifiche)
        self.ui.ButtonAnnullaModifica.clicked.connect(self.close)

    def configura_cliente(self):
        try:
            #Campi comuni
            self.ui.lineEditEmail.setText(self.cliente.email or "")
            self.ui.lineEditTelefono.setText(self.cliente.telefono or "")
            self.ui.lineEditIndirizzo.setText(self.cliente.indirizzo or "")

            #Campi specifici per Cliente Privato
            if self.cliente.is_privato():
                self.ui.stackedWidget.setCurrentIndex(0)
                self.ui.lineEditNome.setText(self.cliente.nome or "")
                self.ui.lineEditCognome.setText(self.cliente.cognome or "")
                self.ui.lineEditCF.setText(self.cliente.cf or "")

            #Campi specifici per Cliente Azienda
            elif self.cliente.is_azienda():
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.lineEditNomeAzienda.setText(self.cliente.nome_azienda or "")
                self.ui.lineEditPartitaIVA.setText(self.cliente.partita_iva or "")

            #Dopo aver impostato la pagina corretta, aggiorna il labelTipoCliente
            self.ui.setTipoCliente(self.cliente.is_privato())

        except AttributeError as e:
            QMessageBox.critical(self, "Errore", f"Errore durante la configurazione cliente: {e}")
            self.close()

        #Collega i campi Codice Fiscale e Partita IVA per la conversione in maiuscolo
        if self.cliente.is_privato():
            self.ui.lineEditCF.textChanged.connect(self.converti_maiuscolo_cf)
        elif self.cliente.is_azienda():
            self.ui.lineEditPartitaIVA.textChanged.connect(self.converti_maiuscolo_piva)

    def converti_maiuscolo_cf(self):
        """Converte il testo del campo Codice Fiscale in maiuscolo."""
        text = self.ui.lineEditCF.text()
        self.ui.lineEditCF.setText(text.upper())

    def converti_maiuscolo_piva(self):
        """Converte il testo del campo Partita IVA in maiuscolo."""
        text = self.ui.lineEditPartitaIVA.text()
        self.ui.lineEditPartitaIVA.setText(text.upper())

    def salva_modifiche(self):
        """
        Salva le modifiche effettuate al cliente, eseguendo anche una validazione dei campi.
        """
        # Valida i campi
        error_message = self.valida_campi_modifica_cliente()
        if error_message:
            QMessageBox.critical(self, "Errore", error_message, QMessageBox.Ok)
            return

        #Aggiorna i dati del cliente
        try:
            if self.cliente.is_privato():
                self.cliente.nome = self.ui.lineEditNome.text().strip()
                self.cliente.cognome = self.ui.lineEditCognome.text().strip()
                self.cliente.cf = self.ui.lineEditCF.text().strip()

            elif self.cliente.is_azienda():
                self.cliente.nome_azienda = self.ui.lineEditNomeAzienda.text().strip()
                self.cliente.partita_iva = self.ui.lineEditPartitaIVA.text().strip()

            self.cliente.email = self.ui.lineEditEmail.text().strip()
            self.cliente.telefono = self.ui.lineEditTelefono.text().strip()
            self.cliente.indirizzo = self.ui.lineEditIndirizzo.text().strip()

            #Aggiorna le informazioni nelle viste collegate
            self.callback_aggiorna_lista()
            self.callback_aggiorna_dettagli()

            #Mostra messaggio di conferma e chiudi la finestra
            QMessageBox.information(self, "Successo", "Modifiche salvate con successo.", QMessageBox.Ok)
            self.close()

        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Errore durante il salvataggio dei dati: {e}", QMessageBox.Ok)

    def valida_campi_modifica_cliente(self):
        """
        Valida i campi della finestra e restituisce un messaggio di errore in caso di problemi.
        """
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        telefono_pattern = r"^\d+$"

        #Validazione campi comuni
        if not self.ui.lineEditEmail.text().strip():
            return "Il campo 'Email' è obbligatorio."
        if not re.match(email_pattern, self.ui.lineEditEmail.text().strip()):
            return "Inserire un'email valida."
        if not self.ui.lineEditTelefono.text().strip():
            return "Il campo 'Telefono' è obbligatorio."
        if not re.match(telefono_pattern, self.ui.lineEditTelefono.text().strip()):
            return "Il campo 'Telefono' deve contenere solo numeri."
        if not self.ui.lineEditIndirizzo.text().strip():
            return "Il campo 'Indirizzo' è obbligatorio."

        #Validazione campi specifici
        if self.cliente.is_privato():
            if not self.ui.lineEditNome.text().strip():
                return "Il campo 'Nome' è obbligatorio per un cliente privato."
            if not self.ui.lineEditCognome.text().strip():
                return "Il campo 'Cognome' è obbligatorio per un cliente privato."

        elif self.cliente.is_azienda():
            if not self.ui.lineEditNomeAzienda.text().strip():
                return "Il campo 'Nome Azienda' è obbligatorio per un cliente azienda."
            if not self.ui.lineEditPartitaIVA.text().strip():
                return "Il campo 'Partita IVA' è obbligatorio per un cliente azienda."

        return None  # Nessun errore trovato

    def dati_modificati(self):
        """
        Verifica se i dati del cliente sono stati modificati rispetto all'originale.
        """
        if self.cliente.is_privato():
            return (
                self.ui.lineEditNome.text() != self.cliente.nome or
                self.ui.lineEditCognome.text() != self.cliente.cognome or
                self.ui.lineEditCF.text() != self.cliente.cf
            )
        elif self.cliente.is_azienda():
            return (
                self.ui.lineEditNomeAzienda.text() != self.cliente.nome_azienda or
                self.ui.lineEditPartitaIVA.text() != self.cliente.partita_iva
            )
        return (
            self.ui.lineEditEmail.text() != self.cliente.email or
            self.ui.lineEditTelefono.text() != self.cliente.telefono or
            self.ui.lineEditIndirizzo.text() != self.cliente.indirizzo
        )

    def chiudi_evento(self, event):
        """
        Gestisce l'evento di chiusura della finestra, verificando modifiche non salvate.
        """
        if self.dati_modificati():
            reply = QMessageBox.question(
                self, "Conferma", "Ci sono modifiche non salvate. Vuoi uscire senza salvare?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
