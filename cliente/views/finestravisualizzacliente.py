# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from cliente.views import img_rc


class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path


class Ui_FinestraVisualizzaCliente(object):
    def configurazioneInteraccia(self, FinestraVisualizzaCliente):
        FinestraVisualizzaCliente.setObjectName("FinestraVisualizzaCliente")
        FinestraVisualizzaCliente.resize(469, 631)
        FinestraVisualizzaCliente.setFixedSize(469, 631)

        self.CentralWidget = QtWidgets.QWidget(FinestraVisualizzaCliente)
        self.CentralWidget.setObjectName("centralwidget")

        #Sfondo con QLabel
        self.label = QtWidgets.QLabel(self.CentralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 471, 631))
        self.label.setPixmap(
            QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg").scaled(
                471, 631, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation
            )
        )
        self.label.setScaledContents(False)  #Evita ulteriori ridimensionamenti dinamici
        self.label.setObjectName("label")

        #Barra in alto
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 471, 41))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        self.BarraAlta.setText("")
        self.BarraAlta.setObjectName("BarraAlta")

        #Label Visualizzazione Cliente
        self.labelVisualizzazioneCliente = QtWidgets.QLabel(self.CentralWidget)
        self.labelVisualizzazioneCliente.setGeometry(QtCore.QRect(120, 10, 241, 20))
        self.labelVisualizzazioneCliente.setStyleSheet("font-family: 'Verdana'; font-size: 20px; color: white;")
        self.labelVisualizzazioneCliente.setObjectName("labelVisualizzazioneCliente")

        #Data
        self.LabelData = QtWidgets.QDateEdit(self.CentralWidget)
        self.LabelData.setGeometry(QtCore.QRect(10, 5, 100, 30))
        self.LabelData.setStyleSheet(self.stileData())
        self.LabelData.setDate(QtCore.QDate.currentDate())
        self.LabelData.setDisplayFormat("dd/MM/yyyy")
        self.LabelData.setCalendarPopup(True)
        self.LabelData.setObjectName("lblDataTime")

        #Definizione dimensioni e posizione delle icone
        larghezzaIcona = 20
        spaziatura = 8
        inizioX = 435
        altezzaBarraAlta = 41  #Altezza della barra
        centroVerticale = (altezzaBarraAlta - larghezzaIcona) // 2  #Calcola il centro verticale

        #Icona Menu Tendina
        self.ButtonTendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.CentralWidget)
        self.ButtonTendina.setGeometry(QtCore.QRect(inizioX, centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonTendina.setObjectName("ButtonTendina")

        #Icona Utente Connesso
        self.ButtonUtenteConnesso = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg",
                                            self.CentralWidget)
        self.ButtonUtenteConnesso.setGeometry(
            QtCore.QRect(inizioX - larghezzaIcona - spaziatura, centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonUtenteConnesso.setObjectName("ButtonUtenteConnesso")

        #Icona Info Software
        self.ButtonInfoSoftware = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.CentralWidget)
        self.ButtonInfoSoftware.setGeometry(
            QtCore.QRect(inizioX - 2 * (larghezzaIcona + spaziatura), centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonInfoSoftware.setObjectName("ButtonInfoSoftware")

        #Radio Buttons
        self.layoutWidget = QtWidgets.QWidget(self.CentralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 70, 181, 31))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayoutTipoCliente = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayoutTipoCliente.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutTipoCliente.setObjectName("horizontalLayoutTipoCliente")

        self.radioPrivato = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioPrivato.setObjectName("radioPrivato")
        self.radioPrivato.setEnabled(False)
        self.horizontalLayoutTipoCliente.addWidget(self.radioPrivato)

        self.radioAzienda = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioAzienda.setObjectName("radioAzienda")
        self.radioAzienda.setEnabled(False)
        self.horizontalLayoutTipoCliente.addWidget(self.radioAzienda)

        #Group Box Dettagli Cliente
        self.groupBoxDettagliCliente = QtWidgets.QGroupBox(self.CentralWidget)
        self.groupBoxDettagliCliente.setGeometry(QtCore.QRect(50, 120, 378, 261))
        self.groupBoxDettagliCliente.setObjectName("groupBoxDettagliCliente")

        self.formLayoutDettagli = QtWidgets.QFormLayout(self.groupBoxDettagliCliente)

        self.labelNome = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelNome.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.formLayoutDettagli.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelNome)
        self.labelNomeValue = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelNomeValue.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelNomeValue.setText("")
        self.formLayoutDettagli.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelNomeValue)

        self.labelCognome = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelCognome.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.formLayoutDettagli.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelCognome)
        self.labelCognomeValue = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelCognomeValue.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelCognomeValue.setText("")
        self.formLayoutDettagli.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelCognomeValue)

        self.labelEmail = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelEmail.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.formLayoutDettagli.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelEmail)
        self.labelEmailValue = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelEmailValue.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelEmailValue.setText("")
        self.formLayoutDettagli.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelEmailValue)

        self.labelTelefono = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelTelefono.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.formLayoutDettagli.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelTelefono)
        self.labelTelefonoValue = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelTelefonoValue.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelTelefonoValue.setText("")
        self.formLayoutDettagli.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelTelefonoValue)

        self.labelIndirizzo = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelIndirizzo.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.formLayoutDettagli.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelIndirizzo)
        self.labelIndirizzoValue = QtWidgets.QLabel(self.groupBoxDettagliCliente)
        self.labelIndirizzoValue.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelIndirizzoValue.setText("")
        self.formLayoutDettagli.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelIndirizzoValue)

        #Bottoni
        self.ButtonModificaCliente = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonModificaCliente.setGeometry(QtCore.QRect(160, 410, 141, 61))
        self.ButtonModificaCliente.setStyleSheet(self.stileButton())
        self.ButtonModificaCliente.setObjectName("ButtonModificaCliente")

        self.ButtonEliminaCliente = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonEliminaCliente.setGeometry(QtCore.QRect(160, 470, 141, 61))
        self.ButtonEliminaCliente.setStyleSheet(self.stileButton())
        self.ButtonEliminaCliente.setObjectName("ButtonEliminaCliente")

        self.ButtonChiudi = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonChiudi.setGeometry(QtCore.QRect(160, 530, 141, 61))
        self.ButtonChiudi.setStyleSheet(self.stileButton())
        self.ButtonChiudi.setObjectName("ButtonChiudi")

        FinestraVisualizzaCliente.setCentralWidget(self.CentralWidget)
        self.aggiornaTestiInterfaccia(FinestraVisualizzaCliente)
        QtCore.QMetaObject.connectSlotsByName(FinestraVisualizzaCliente)

    def configuraCampiCliente(self, cliente):
        """
        Configura la finestra in base al tipo di cliente.
        """
        try:
            #Log di debug
            print(f"Configurazione campi cliente: {cliente.id}")

            #Valori comuni
            self.labelEmailValue.setText(cliente.email or "Non disponibile")
            self.labelTelefonoValue.setText(cliente.telefono or "Non disponibile")
            self.labelIndirizzoValue.setText(cliente.indirizzo or "Non disponibile")

            #Tipo di cliente
            if cliente.is_privato():
                self.radioPrivato.setChecked(True)
                self.labelNome.setText("Nome:")
                self.labelNomeValue.setText(cliente.nome or "Non disponibile")
                self.labelCognome.setText("Cognome:")
                self.labelCognomeValue.setText(cliente.cognome or "Non disponibile")

                #Codice Fiscale per Cliente Privato
                if not hasattr(self, 'labelCodiceFiscale'):
                    self.labelCodiceFiscaleTitle = QtWidgets.QLabel(self.groupBoxDettagliCliente)
                    self.labelCodiceFiscaleTitle.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
                    self.labelCodiceFiscaleTitle.setText("Codice Fiscale:")

                    self.labelCodiceFiscale = QtWidgets.QLabel(self.groupBoxDettagliCliente)
                    self.labelCodiceFiscale.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")

                    self.formLayoutDettagli.addRow(self.labelCodiceFiscaleTitle, self.labelCodiceFiscale)

                self.labelCodiceFiscale.setText(cliente.cf or "Non disponibile")

            elif cliente.is_azienda():
                self.radioAzienda.setChecked(True)
                self.labelNome.setText("Nome Azienda:")
                self.labelNomeValue.setText(cliente.nome_azienda or "Non disponibile")
                self.labelCognome.setText("Partita IVA:")
                self.labelCognomeValue.setText(cliente.partita_iva or "Non disponibile")
            else:
                raise ValueError("Tipo di cliente non riconosciuto.")
        except Exception as e:
            print(f"Errore nella configurazione dei campi cliente: {e}")

    def aggiornaTestiInterfaccia(self, FinestraVisualizzaCliente):
        trad = QtCore.QCoreApplication.translate

        #Imposta il titolo della finestra
        FinestraVisualizzaCliente.setWindowTitle(trad("FinestraVisualizzaCliente", "Visualizzazione Cliente"))

        #Titolo nella barra superiore
        self.labelVisualizzazioneCliente.setText(trad("FinestraVisualizzaCliente", "Visualizzazione Cliente"))

        #Radio buttons per tipo cliente
        self.radioPrivato.setText(trad("FinestraVisualizzaCliente", "Privato"))
        self.radioAzienda.setText(trad("FinestraVisualizzaCliente", "Azienda"))

        #Titolo del groupbox dei dettagli
        self.groupBoxDettagliCliente.setTitle(trad("FinestraVisualizzaCliente", "Dettagli Cliente"))

        #Etichette dei dettagli cliente
        self.labelNome.setText(trad("FinestraVisualizzaCliente", "Nome:"))
        self.labelCognome.setText(trad("FinestraVisualizzaCliente", "Cognome:"))
        self.labelEmail.setText(trad("FinestraVisualizzaCliente", "Email:"))
        self.labelTelefono.setText(trad("FinestraVisualizzaCliente", "Telefono:"))
        self.labelIndirizzo.setText(trad("FinestraVisualizzaCliente", "Indirizzo:"))

        #Testi dei pulsanti
        self.ButtonModificaCliente.setText(trad("FinestraVisualizzaCliente", "Modifica"))
        self.ButtonEliminaCliente.setText(trad("FinestraVisualizzaCliente", "Elimina"))
        self.ButtonChiudi.setText(trad("FinestraVisualizzaCliente", "Chiudi"))

    def stileButton(self):
        return """
            QPushButton {
                background-color: #283747;
                border-radius: 8px;
                border: 3px solid white;
                color: white;
                padding: 8px;
                font-size: 17px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #1E2230;
            }
            QPushButton:focus {
                background-color: #242835;
                border-color: white;
            }
        """
    def stileData(self):
        return """
        QDateEdit {
            font-family: 'Montserrat', sans-serif;
            font-size: 10px;
            font-weight: 600;
            color: white;
            background-color: rgba(0, 0, 0, 0); /* Trasparente per fondersi con lo sfondo */
            border: 1px solid white; /* Bordo bianco per visibilità */
            border-radius: 4px; /* Angoli arrotondati */
        }
        """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FinestraVisualizzaCliente = QtWidgets.QMainWindow()
    ui = Ui_FinestraVisualizzaCliente()
    ui.configurazioneInteraccia(FinestraVisualizzaCliente)
    FinestraVisualizzaCliente.show()
    sys.exit(app.exec_())
