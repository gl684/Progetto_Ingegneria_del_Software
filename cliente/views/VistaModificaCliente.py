from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox

class VistaModificaCliente(QWidget):
    def __init__(self, cliente, callback_aggiorna_lista, callback_aggiorna_dettagli, parent=None):
        super(VistaModificaCliente, self).__init__(parent)

        self.cliente = cliente
        self.callback_aggiorna_lista = callback_aggiorna_lista
        self.callback_aggiorna_dettagli = callback_aggiorna_dettagli

        self.init_ui()

        # Separiamo la finestra di modifica del cliente dal genitore
        self.setParent(None)  # Rende questa finestra indipendente dalla finestra principale

    def init_ui(self):
        v_layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Campi di input con i dati precompilati del cliente
        self.email_edit = QLineEdit(self.cliente.email)
        self.telefono_edit = QLineEdit(self.cliente.telefono)

        form_layout.addRow(QLabel("Email:"), self.email_edit)
        form_layout.addRow(QLabel("Telefono:"), self.telefono_edit)

        if self.cliente.is_privato():
            self.nome_edit = QLineEdit(self.cliente.nome)
            self.cognome_edit = QLineEdit(self.cliente.cognome)
            form_layout.addRow(QLabel("Nome:"), self.nome_edit)
            form_layout.addRow(QLabel("Cognome:"), self.cognome_edit)
        elif self.cliente.is_azienda():
            self.nome_azienda_edit = QLineEdit(self.cliente.nome_azienda)
            self.partita_iva_edit = QLineEdit(self.cliente.partita_iva)
            form_layout.addRow(QLabel("Nome Azienda:"), self.nome_azienda_edit)
            form_layout.addRow(QLabel("Partita IVA:"), self.partita_iva_edit)

        v_layout.addLayout(form_layout)

        # Bottone per confermare le modifiche
        save_button = QPushButton("Salva Modifiche")
        save_button.clicked.connect(self.salva_modifiche)
        v_layout.addWidget(save_button)

        self.setLayout(v_layout)
        self.setWindowTitle("Modifica Cliente")
        self.resize(400, 300)

    def salva_modifiche(self):
        # Aggiorna i dati del cliente con i valori dei campi
        self.cliente.email = self.email_edit.text()
        self.cliente.telefono = self.telefono_edit.text()

        if self.cliente.is_privato():
            self.cliente.nome = self.nome_edit.text()
            self.cliente.cognome = self.cognome_edit.text()
        elif self.cliente.is_azienda():
            self.cliente.nome_azienda = self.nome_azienda_edit.text()
            self.cliente.partita_iva = self.partita_iva_edit.text()

        # Fai un controllo di validità sui campi
        if not self.cliente.email or not self.cliente.telefono:
            QMessageBox.critical(self, 'Errore', 'Compila tutti i campi!', QMessageBox.Ok)
            return

        # Salva le modifiche, aggiorna la lista clienti e i dettagli
        self.callback_aggiorna_lista()  # Aggiorna la lista clienti
        self.callback_aggiorna_dettagli()  # Aggiorna i dettagli nella finestra del cliente

        # Chiudi la finestra
        self.close()
