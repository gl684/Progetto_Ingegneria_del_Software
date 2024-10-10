from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem

from ordine.controller.ControlloreOrdine import ControlloreOrdine


class VistaOrdine(QWidget):
    def __init__(self, ordine):
        super().__init__()

        # Inizializza il controller per l'ordine
        self.controller = ControlloreOrdine(ordine)

        # Layout principale
        layout = QVBoxLayout()

        # Aggiungi dettagli dell'ordine
        layout.addWidget(QLabel(f"Nome Ordine: {self.controller.get_nome_ordine()}"))
        layout.addWidget(QLabel(f"Oggetto Ordine: {self.controller.get_oggetto_ordine()}"))
        layout.addWidget(QLabel(f"Data Inizio: {self.controller.get_data_inizio()}"))
        layout.addWidget(QLabel(f"Data Termine: {self.controller.get_data_termine()}"))
        layout.addWidget(QLabel(f"Stato: {self.controller.get_stato()}"))

        # Aggiungi la lista delle fasi
        fasi_label = QLabel("Fasi dell'Ordine:")
        layout.addWidget(fasi_label)
        self.fasi_list = QListWidget()
        for fase in self.controller.get_fasi():
            item = QListWidgetItem(f"Fase {fase.numero_fase}: {fase.nome_fase} - Stato: {fase.stato_fase}")
            self.fasi_list.addItem(item)
        layout.addWidget(self.fasi_list)

        # Imposta il layout della finestra
        self.setLayout(layout)
        self.setWindowTitle(f"Dettagli Ordine: {self.controller.get_nome_ordine()}")
        self.resize(400, 300)