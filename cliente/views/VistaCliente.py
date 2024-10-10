from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QGroupBox, QFrame

from cliente.views.VistaModificaCliente import VistaModificaCliente


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_cliente_callback, aggiorna_lista_clienti_callback, parent=None):
        super(VistaCliente, self).__init__(parent)

        self.cliente = cliente
        self.elimina_cliente_callback = elimina_cliente_callback
        self.aggiorna_lista_clienti_callback = aggiorna_lista_clienti_callback

        self.init_ui()

        # Separiamo la finestra di modifica del cliente dal genitore
        self.setParent(None)  # Rende questa finestra indipendente dalla finestra principale

    def init_ui(self):
        self.v_layout = QVBoxLayout()

        # Sezione informazioni cliente
        self.info_cliente_group = QGroupBox("Dettagli Cliente")
        self.info_layout = QFormLayout()

        # Chiamo la funzione per impostare i dettagli cliente
        self.aggiorna_dettagli_cliente()

        self.info_cliente_group.setLayout(self.info_layout)
        self.v_layout.addWidget(self.info_cliente_group)

        # Bottone per modificare il cliente
        modifica_button = QPushButton("Modifica")
        modifica_button.clicked.connect(self.modifica_cliente)  # Collegamento alla funzione modifica
        self.v_layout.addWidget(modifica_button)

        # Bottone per eliminare il cliente
        delete_button = QPushButton("Elimina")
        delete_button.clicked.connect(self.elimina_cliente)
        self.v_layout.addWidget(delete_button)

        # Bottone per chiudere la finestra
        close_button = QPushButton("Chiudi")
        close_button.clicked.connect(self.close)
        self.v_layout.addWidget(close_button)

        self.setLayout(self.v_layout)
        self.setWindowTitle(f"Dettagli Cliente - {self.cliente.id}")
        self.resize(400, 400)

    def aggiorna_dettagli_cliente(self):
        """Aggiorna i campi della finestra con i dettagli aggiornati del cliente"""
        # Pulire il layout esistente per aggiornare i dati
        for i in reversed(range(self.info_layout.count())):
            widget = self.info_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Aggiungi informazioni base del cliente
        self.info_layout.addRow(QLabel("ID Cliente:"), QLabel(self.cliente.id))
        self.info_layout.addRow(QLabel("Email:"), QLabel(self.cliente.email))
        self.info_layout.addRow(QLabel("Telefono:"), QLabel(self.cliente.telefono))
        self.info_layout.addRow(QLabel("Tipo Cliente:"), QLabel(self.cliente.tipo_cliente))

        # Aggiungi descrizione cliente in un formato multilinea
        descrizione_cliente = QLabel(self.formatta_descrizione_cliente())
        descrizione_cliente.setWordWrap(True)  # Permette al testo di andare a capo
        self.info_layout.addRow(QLabel("Descrizione Cliente:"), descrizione_cliente)

    def formatta_descrizione_cliente(self):
        """Crea una descrizione su più righe per il cliente"""
        if self.cliente.is_privato():
            return (f"Nome: {self.cliente.nome}\n"
                    f"Cognome: {self.cliente.cognome}\n"
                    f"Codice Fiscale: {self.cliente.cf}\n"
                    f"Indirizzo: {self.cliente.indirizzo}\n"
                    f"Email: {self.cliente.email}\n"
                    f"Telefono: {self.cliente.telefono}")
        elif self.cliente.is_azienda():
            return (f"Nome Azienda: {self.cliente.nome_azienda}\n"
                    f"Partita IVA: {self.cliente.partita_iva}\n"
                    f"Indirizzo Azienda: {self.cliente.indirizzo_azienda}\n"
                    f"Email: {self.cliente.email}\n"
                    f"Telefono: {self.cliente.telefono}")
        else:
            return "Tipo di cliente sconosciuto."

    def elimina_cliente(self):
        # Esegui la callback per eliminare il cliente e aggiorna la lista
        self.elimina_cliente_callback(self.cliente.id)
        self.aggiorna_lista_clienti_callback()
        self.close()

    def modifica_cliente(self):
        # Passiamo anche la funzione 'aggiorna_dettagli_cliente' come callback
        self.vista_modifica = VistaModificaCliente(self.cliente, self.aggiorna_lista_clienti_callback, self.aggiorna_dettagli_cliente, self)

        # Mostriamo la finestra di modifica del cliente
        self.vista_modifica.show()
