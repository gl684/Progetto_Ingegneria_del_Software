from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QListView, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt

from listaordini.controller.ControlloreListaOrdini import ControlloreListaOrdini
from ordine.views.VistaOrdine import VistaOrdine

class VistaListaOrdini(QWidget):
    def __init__(self):
        super().__init__()

        # Inizializza il controllore
        self.controller = ControlloreListaOrdini()

        # Layout principale
        h_layout = QHBoxLayout()

        # Layout verticale per il filtro
        v_filter_layout = QVBoxLayout()

        # Label per il filtro
        filter_label = QLabel("Filtra per tipo:")
        v_filter_layout.addWidget(filter_label)

        # Combo box per il filtro
        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItem("Tutti")  # Aggiungi l'opzione "Tutti" inizialmente
        self.populate_filter_options()  # Popola dinamicamente i tipi di ordini
        self.filter_combo_box.currentIndexChanged.connect(self.apply_filter)
        v_filter_layout.addWidget(self.filter_combo_box)

        # Lista ordini
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.listview_model)
        v_filter_layout.addWidget(self.list_view)

        # Aggiungi il layout di filtro e lista al layout principale
        h_layout.addLayout(v_filter_layout)

        # Layout verticale per i bottoni
        buttons_layout = QVBoxLayout()
        open_button = QPushButton("Visualizza Ordine")
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)
        open_button.clicked.connect(self.show_ordine_details)

        self.setLayout(h_layout)
        self.resize(800, 400)
        self.setWindowTitle("Lista Ordini")

        # Inizializza la lista degli ordini e carica i dati
        self.display_ordini(self.controller.get_lista_degli_ordini())

    def populate_filter_options(self):
        """Popola dinamicamente la combo box con i tipi di ordini unici."""
        ordini = self.controller.get_lista_degli_ordini()
        tipi_ordini = set([ordine.oggetto_ordine for ordine in ordini])  # Trova i tipi unici
        self.filter_combo_box.addItems(tipi_ordini)  # Aggiungi i tipi unici alla combo box

    def display_ordini(self, ordini):
        """Visualizza gli ordini nella lista."""
        self.listview_model.clear()
        for ordine in ordini:
            item = QStandardItem()
            item.setText(f"{ordine.nome_ordine} - {ordine.oggetto_ordine}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)

    def apply_filter(self):
        """Applica il filtro in base alla selezione nella ComboBox."""
        filtro = self.filter_combo_box.currentText()

        if filtro == "Tutti":
            # Se "Tutti" è selezionato, mostra tutti gli ordini
            self.display_ordini(self.controller.get_lista_degli_ordini())
        else:
            # Filtra gli ordini per tipo di oggetto_ordine
            ordini_filtrati = self.controller.get_lista_degli_ordini_filtrata(filtro)
            self.display_ordini(ordini_filtrati)

    def show_ordine_details(self):
        """Mostra i dettagli dell'ordine selezionato."""
        selected_index = self.list_view.currentIndex().row()

        if selected_index < 0:
            QMessageBox.warning(self, "Errore", "Seleziona un ordine prima di visualizzarlo")
        else:
            ordine = self.controller.get_ordine_by_index(selected_index)
            self.vista_ordine = VistaOrdine(ordine)
            self.vista_ordine.show()

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()  # Permetti la chiusura della finestra
