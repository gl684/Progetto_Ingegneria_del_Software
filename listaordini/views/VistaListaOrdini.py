from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from listaordini.views.finestralistaordini import Ui_FinestraListaOrdini
from listaordini.controller.ControlloreListaOrdini import ControlloreListaOrdini
from ordine.views.VistaOrdine import VistaOrdine


class VistaListaOrdini(QMainWindow):
    def __init__(self, parent=None):
        super(VistaListaOrdini, self).__init__(parent)

        # Inizializza l'interfaccia grafica generata
        self.ui = Ui_FinestraListaOrdini()
        self.ui.configurazioneInterfaccia(self)

        # Inizializza il controller
        self.controller = ControlloreListaOrdini()

        # Collega i pulsanti e i filtri agli eventi
        self.ui.ButtonVisualizzaOrdine.clicked.connect(self.mostra_info_ordine)
        self.ui.comboBoxFiltroTipoOrdine.currentIndexChanged.connect(self.applica_filtro)

        # Popola i dati iniziali
        self.popola_opzioni_filtro()

        # Applica l'opzione di default del filtro
        self.applica_filtro()  # Forza il popolamento iniziale della lista

    def popola_opzioni_filtro(self):
        """Popola dinamicamente la combo box con i tipi di ordini unici."""
        self.ui.comboBoxFiltroTipoOrdine.clear()
        self.ui.comboBoxFiltroTipoOrdine.addItem("Tutti")  # Opzione per visualizzare tutti gli ordini
        ordini = self.controller.get_lista_degli_ordini()
        tipi_ordini = set(ordine.oggetto_ordine for ordine in ordini)
        self.ui.comboBoxFiltroTipoOrdine.addItems(sorted(tipi_ordini))  # Ordina alfabeticamente

    def aggiorna_lista_ordini(self):
        """Aggiorna la lista degli ordini nella QListWidget."""
        self.ui.ListaOrdini.clear()
        ordini = self.controller.get_lista_degli_ordini()
        if not ordini:
            self.ui.ListaOrdini.addItem("Nessun ordine presente.")
            return

        for ordine in ordini:
            item = QListWidgetItem(f"{ordine.nome_ordine} - {ordine.oggetto_ordine}")
            self.ui.ListaOrdini.addItem(item)

    def applica_filtro(self):
        """Applica il filtro in base alla selezione nella ComboBox."""
        try:
            filtro = self.ui.comboBoxFiltroTipoOrdine.currentText()
            print(f"Filtro applicato: {filtro}")  # Debug

            if filtro == "Tutti":
                ordini_filtrati = self.controller.get_lista_degli_ordini()
            else:
                ordini_filtrati = self.controller.get_lista_degli_ordini_filtrata(filtro)

            self.ui.ListaOrdini.clear()

            if not ordini_filtrati:
                item = QListWidgetItem("Nessun ordine corrispondente al filtro selezionato.")
                item.setFlags(QtCore.Qt.NoItemFlags)  # Rendi l'elemento non selezionabile
                self.ui.ListaOrdini.addItem(item)
                print("Nessun ordine corrispondente trovato.")  # Debug
                return

            for ordine in ordini_filtrati:
                item = QListWidgetItem(f"{ordine.nome_ordine} - {ordine.oggetto_ordine}")
                self.ui.ListaOrdini.addItem(item)

            # Deseleziona qualsiasi elemento nella lista
            self.ui.ListaOrdini.clearSelection()
            print("Filtro applicato correttamente.")  # Debug

        except Exception as e:
            print(f"Errore durante l'applicazione del filtro: {e}")  # Debug dell'errore
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore durante l'applicazione del filtro: {e}")

    def mostra_info_ordine(self):
        """Mostra i dettagli dell'ordine selezionato."""
        try:
            # Ottieni l'elemento selezionato
            item_selezionato = self.ui.ListaOrdini.currentItem()

            # Controlla se è stato selezionato un elemento
            if not item_selezionato or not item_selezionato.isSelected():
                QMessageBox.warning(self, "Avviso", "Non hai selezionato alcun ordine.")  # Messaggio di avviso
                return  # Esci dal metodo

            # Controlla se il testo dell'elemento selezionato è un messaggio di lista vuota
            if item_selezionato.text() in ["Nessun ordine presente.",
                                        "Nessun ordine corrispondente al filtro selezionato."]:
                QMessageBox.warning(self, "Avviso", "Non hai selezionato alcun ordine valido.")  # Messaggio di avviso
                return  # Esci dal metodo

            # Determina la lista corrente in base al filtro
            filtro = self.ui.comboBoxFiltroTipoOrdine.currentText()
            if filtro == "Tutti":
                lista_ordini = self.controller.get_lista_degli_ordini()
            else:
                lista_ordini = self.controller.get_lista_degli_ordini_filtrata(filtro)

            # Ottieni l'indice dell'elemento selezionato nella lista visibile
            index_selezionato = self.ui.ListaOrdini.row(item_selezionato)

            # Controlla se l'indice è valido rispetto alla lista corrente
            if index_selezionato < 0 or index_selezionato >= len(lista_ordini):
                QMessageBox.warning(self, "Avviso",
                                    "Selezione non valida. Per favore seleziona un ordine.")  # Messaggio di avviso
                return  # Esci dal metodo

            # Ottieni l'ordine corrispondente
            ordine_selezionato = lista_ordini[index_selezionato]

            if not ordine_selezionato:
                QMessageBox.critical(self, "Errore", "Ordine non trovato.")  # Messaggio di errore critico
                return  # Esci dal metodo

            # Mostra la finestra dei dettagli dell'ordine
            self.vista_ordine = VistaOrdine(ordine_selezionato)
            self.vista_ordine.setWindowModality(QtCore.Qt.ApplicationModal)
            self.vista_ordine.show()

        except Exception as e:
            QMessageBox.critical(self, "Errore", f"Si è verificato un errore: {e}")

    def chiudi_evento(self, event):
        """Salva i dati alla chiusura della finestra."""
        self.controller.salva_dati()
        event.accept()
