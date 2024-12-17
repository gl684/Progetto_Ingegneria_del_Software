from PyQt5 import QtWidgets, QtCore
from cliente.views.VistaModificaCliente import VistaModificaCliente
from cliente.views.finestravisualizzacliente import Ui_FinestraVisualizzaCliente


class VistaCliente(QtWidgets.QMainWindow):
    def __init__(self, cliente, elimina_cliente_callback, aggiorna_lista_clienti_callback, parent=None):
        super(VistaCliente, self).__init__(parent)

        self.cliente = cliente
        self.elimina_cliente_callback = elimina_cliente_callback
        self.aggiorna_lista_clienti_callback = aggiorna_lista_clienti_callback

        #Inizializza l'interfaccia utente
        self.ui = Ui_FinestraVisualizzaCliente()
        self.ui.configurazioneInteraccia(self)

        #Popola i dettagli del cliente
        self.popola_dettagli_cliente()

        #Collega i pulsanti a funzioni
        self.ui.ButtonChiudi.clicked.connect(self.close)
        self.ui.ButtonModificaCliente.clicked.connect(self.modifica_cliente)
        self.ui.ButtonEliminaCliente.clicked.connect(self.elimina_cliente)

        #Configura la finestra
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle(f"Dettagli Cliente - {self.cliente.id}")

    def popola_dettagli_cliente(self):
        """
        Popola i dettagli del cliente nei widget della finestra.
        """
        try:
            self.ui.configuraCampiCliente(self.cliente)
        except Exception as e:
            print(f"Errore durante la configurazione dei campi cliente: {e}")

    def modifica_cliente(self):
        """
        Mostra la finestra per modificare i dettagli del cliente.
        """
        try:
            print("Apertura VistaModificaCliente")
            self.vista_modifica_cliente = VistaModificaCliente(
                cliente=self.cliente,
                callback_aggiorna_lista=self.aggiorna_lista_clienti_callback,
                callback_aggiorna_dettagli=self.popola_dettagli_cliente,
                parent=self
            )
            self.vista_modifica_cliente.setWindowModality(QtCore.Qt.ApplicationModal)
            self.vista_modifica_cliente.show()
        except Exception as e:
            print(f"Errore durante l'apertura di VistaModificaCliente: {e}")

    def elimina_cliente(self):
        """
        Esegue l'eliminazione del cliente.
        """
        try:
            self.elimina_cliente_callback(self.cliente.id)
            self.aggiorna_lista_clienti_callback()
            self.close()
        except Exception as e:
            print(f"Errore durante l'eliminazione del cliente: {e}")
