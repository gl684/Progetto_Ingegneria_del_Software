from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QComboBox
from cliente.model.Cliente import Cliente

class VistaInserisciCliente(QWidget):
    def __init__(self, controller, callback, parent=None):  # Aggiungi 'parent=None'
        super(VistaInserisciCliente, self).__init__(parent)  # Passa 'parent' al costruttore QWidget
        self.controller = controller
        self.callback = callback
        self.info = {}

        self.v_layout = QVBoxLayout()

        # Aggiungi un campo per la selezione del tipo di cliente
        self.tipo_cliente_combo = QComboBox(self)
        self.tipo_cliente_combo.addItems(["Privato", "Azienda"])
        self.tipo_cliente_combo.currentIndexChanged.connect(self.toggle_fields)
        self.v_layout.addWidget(QLabel("Tipo Cliente"))
        self.v_layout.addWidget(self.tipo_cliente_combo)

        # Campi per cliente privato
        self.get_form_entry("Nome")
        self.get_form_entry("Cognome")
        self.get_form_entry("Codice Fiscale")
        self.get_form_entry("Indirizzo")

        # Campi per cliente azienda
        self.get_form_entry("Nome Azienda")
        self.get_form_entry("Partita IVA")
        self.get_form_entry("Indirizzo Azienda")

        # Campi comuni a entrambi i tipi di cliente
        self.get_form_entry("Email")
        self.get_form_entry("Telefono")

        # Inizialmente nascondi i campi per azienda
        self.toggle_fields()

        # Aggiungi un pulsante OK per l'inserimento
        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_cliente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Cliente")

    def get_form_entry(self, tipo):
        """Metodo per creare un campo di input."""
        self.v_layout.addWidget(QLabel(tipo))
        current_text_edit = QLineEdit(self)
        self.v_layout.addWidget(current_text_edit)
        self.info[tipo] = current_text_edit

    def toggle_fields(self):
        """Nasconde o mostra i campi in base al tipo di cliente selezionato."""
        tipo_cliente = self.tipo_cliente_combo.currentText()

        # Nascondi o mostra i campi specifici per privato e azienda
        is_privato = (tipo_cliente == "Privato")
        self.info["Nome"].setVisible(is_privato)
        self.info["Cognome"].setVisible(is_privato)
        self.info["Codice Fiscale"].setVisible(is_privato)
        self.info["Indirizzo"].setVisible(is_privato)

        self.info["Nome Azienda"].setVisible(not is_privato)
        self.info["Partita IVA"].setVisible(not is_privato)
        self.info["Indirizzo Azienda"].setVisible(not is_privato)

    def add_cliente(self):
        tipo_cliente = self.tipo_cliente_combo.currentText()

        # Dati comuni
        email = self.info["Email"].text()
        telefono = self.info["Telefono"].text()

        # Controlla se i campi comuni sono vuoti
        if email == "" or telefono == "":
            QMessageBox.critical(self, 'Errore', 'Inserisci email e telefono.', QMessageBox.Ok, QMessageBox.Ok)
            return

        if tipo_cliente == "Privato":
            nome = self.info["Nome"].text()
            cognome = self.info["Cognome"].text()
            cf = self.info["Codice Fiscale"].text()
            indirizzo = self.info["Indirizzo"].text()

            if nome == "" or cognome == "" or cf == "" or indirizzo == "":
                QMessageBox.critical(self, 'Errore',
                                     'Per favore, inserisci tutte le informazioni richieste per il cliente privato',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

            cliente = Cliente(id=(nome + cognome).lower(), email=email, telefono=telefono, tipo_cliente="Privato",
                              nome=nome, cognome=cognome, cf=cf, indirizzo=indirizzo)

        elif tipo_cliente == "Azienda":
            nome_azienda = self.info["Nome Azienda"].text()
            partita_iva = self.info["Partita IVA"].text()
            indirizzo_azienda = self.info["Indirizzo Azienda"].text()

            if nome_azienda == "" or partita_iva == "" or indirizzo_azienda == "":
                QMessageBox.critical(self, 'Errore',
                                     'Per favore, inserisci tutte le informazioni richieste per l\'azienda',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

            cliente = Cliente(id=nome_azienda.lower(), email=email, telefono=telefono, tipo_cliente="Azienda",
                              nome_azienda=nome_azienda, partita_iva=partita_iva, indirizzo_azienda=indirizzo_azienda)

        # Aggiungi il cliente, aggiorna la vista e salva i dati
        self.controller.aggiungi_cliente(cliente)
        self.controller.save_data()  # Salva i dati subito
        self.callback()
        self.close()