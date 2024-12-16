from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from PyQt5.QtGui import QPixmap


class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path

class Ui_FinestraInserisciCliente(object):
    def configurazioneInterfaccia(self, FinestraInserisciCliente):
        FinestraInserisciCliente.setObjectName("FinestraInserisciCliente")
        FinestraInserisciCliente.resize(561, 550)  # Altezza aumentata
        FinestraInserisciCliente.setFixedSize(561, 550)

        # **Widget centrale**
        self.CentralWidget = QtWidgets.QWidget(FinestraInserisciCliente)
        self.CentralWidget.setObjectName("CentralWidget")

        # **Sfondo immagine principale**
        self.label = QtWidgets.QLabel(self.CentralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 561, 550))
        self.label.setStyleSheet("background-color: black;")
        self.label.setPixmap(QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        # **Barra Alta**
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.BarraAlta.setStyleSheet("""
            QLabel {
                background-color: #283747;
                border-bottom: 2px solid white;
            }
        """)
        self.BarraAlta.setText("")
        self.BarraAlta.setObjectName("BarraAlta")

        self.labelNuovoCliente = QtWidgets.QLabel(self.CentralWidget)
        self.labelNuovoCliente.setGeometry(QtCore.QRect(190, 10, 171, 20))
        self.labelNuovoCliente.setStyleSheet("""
            QLabel {
                font-family: 'Verdana';
                font-size: 24px;
                color: #FFFFFF;
            }
        """)
        self.labelNuovoCliente.setText("Nuovo Cliente")
        self.labelNuovoCliente.setObjectName("labelNuovoCliente")

        # Data
        self.LabelData = QtWidgets.QDateEdit(self.CentralWidget)
        self.LabelData.setGeometry(QtCore.QRect(10, 5, 100, 30))  # Posizionamento corretto
        self.LabelData.setStyleSheet(self.stileData())
        self.LabelData.setDate(QtCore.QDate.currentDate())
        self.LabelData.setDisplayFormat("dd/MM/yyyy")
        self.LabelData.setCalendarPopup(True)
        self.LabelData.setObjectName("lblDataTime")

        # Definizione dimensioni e posizione delle icone
        larghezzaIcona = 20
        spaziatura = 8
        inizioX = 530
        altezzaBarraAlta = 41  # Altezza della barra
        centroVerticale = (altezzaBarraAlta - larghezzaIcona) // 2  # Calcola il centro verticale

        # Icona Menu Tendina
        self.ButtonTendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.CentralWidget)
        self.ButtonTendina.setGeometry(QtCore.QRect(inizioX, centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonTendina.setObjectName("ButtonTendina")

        # Icona Utente Connesso
        self.ButtonUtenteConnesso = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg",
                                            self.CentralWidget)
        self.ButtonUtenteConnesso.setGeometry(
            QtCore.QRect(inizioX - larghezzaIcona - spaziatura, centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonUtenteConnesso.setObjectName("ButtonUtenteConnesso")

        # Icona Info Software
        self.ButtonInfoSoftware = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.CentralWidget)
        self.ButtonInfoSoftware.setGeometry(
            QtCore.QRect(inizioX - 2 * (larghezzaIcona + spaziatura), centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonInfoSoftware.setObjectName("ButtonInfoSoftware")

        # **Tipo Cliente**
        self.labelTipoCliente = QtWidgets.QLabel(self.CentralWidget)
        self.labelTipoCliente.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelTipoCliente.setGeometry(QtCore.QRect(40, 80, 100, 22))
        self.labelTipoCliente.setText("Tipo Cliente:")
        self.comboBoxTipoCliente = QtWidgets.QComboBox(self.CentralWidget)
        self.comboBoxTipoCliente.setGeometry(QtCore.QRect(180, 80, 296, 22))
        self.comboBoxTipoCliente.addItems(["Privato", "Azienda"])
        self.comboBoxTipoCliente.setObjectName("comboBoxTipoCliente")

        # **Campi Comuni**
        self.labelIndirizzo = QtWidgets.QLabel(self.CentralWidget)
        self.labelIndirizzo.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelIndirizzo.setGeometry(QtCore.QRect(40, 150, 80, 22))
        self.labelIndirizzo.setText("Indirizzo:")
        self.lineEditIndirizzo = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditIndirizzo.setGeometry(QtCore.QRect(180, 150, 296, 22))

        self.labelTelefono = QtWidgets.QLabel(self.CentralWidget)
        self.labelTelefono.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelTelefono.setGeometry(QtCore.QRect(40, 200, 80, 22))
        self.labelTelefono.setText("Telefono:")
        self.lineEditTelefono = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditTelefono.setGeometry(QtCore.QRect(180, 200, 296, 22))

        self.labelEmail = QtWidgets.QLabel(self.CentralWidget)
        self.labelEmail.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelEmail.setGeometry(QtCore.QRect(40, 250, 80, 22))
        self.labelEmail.setText("Email:")
        self.lineEditEmail = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(180, 250, 296, 22))

        # **Campi Cliente Privato**
        self.labelNome = QtWidgets.QLabel(self.CentralWidget)
        self.labelNome.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelNome.setGeometry(QtCore.QRect(40, 300, 80, 22))
        self.labelNome.setText("Nome:")
        self.lineEditNome = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditNome.setGeometry(QtCore.QRect(180, 300, 296, 22))

        self.labelCognome = QtWidgets.QLabel(self.CentralWidget)
        self.labelCognome.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelCognome.setGeometry(QtCore.QRect(40, 350, 80, 22))
        self.labelCognome.setText("Cognome:")
        self.lineEditCognome = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditCognome.setGeometry(QtCore.QRect(180, 350, 296, 22))

        self.labelCF = QtWidgets.QLabel(self.CentralWidget)
        self.labelCF.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelCF.setGeometry(QtCore.QRect(40, 400, 110, 22))
        self.labelCF.setText("Codice Fiscale:")
        self.lineEditCF = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditCF.setGeometry(QtCore.QRect(180, 400, 296, 22))

        # **Campi Cliente Azienda**
        self.labelNomeAzienda = QtWidgets.QLabel(self.CentralWidget)
        self.labelNomeAzienda.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelNomeAzienda.setGeometry(QtCore.QRect(40, 300, 110, 22))
        self.labelNomeAzienda.setText("Nome Azienda:")
        self.lineEditNomeAzienda = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditNomeAzienda.setGeometry(QtCore.QRect(180, 300, 296, 22))

        self.labelPartitaIVA = QtWidgets.QLabel(self.CentralWidget)
        self.labelPartitaIVA.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelPartitaIVA.setGeometry(QtCore.QRect(40, 350, 110, 22))
        self.labelPartitaIVA.setText("Partita IVA:")
        self.lineEditPartitaIVA = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEditPartitaIVA.setGeometry(QtCore.QRect(180, 350, 296, 22))

        # **Bottoni**
        self.ButtonConferma = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonConferma.setGeometry(QtCore.QRect(90, 460, 171, 50))  # Posizionato più in basso
        self.ButtonConferma.setStyleSheet(self.stileButton())  # Applica lo stile
        self.ButtonConferma.setText("Conferma")

        self.ButtonAnnulla = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonAnnulla.setGeometry(QtCore.QRect(300, 460, 171, 50))  # Posizionato più in basso
        self.ButtonAnnulla.setStyleSheet(self.stileButton())  # Applica lo stile
        self.ButtonAnnulla.setText("Annulla")

        # **Logica di Default**
        self.labelNome.hide()
        self.lineEditNome.hide()
        self.labelCognome.hide()
        self.lineEditCognome.hide()
        self.labelCF.hide()
        self.lineEditCF.hide()

        self.labelNomeAzienda.hide()
        self.lineEditNomeAzienda.hide()
        self.labelPartitaIVA.hide()
        self.lineEditPartitaIVA.hide()

        FinestraInserisciCliente.setCentralWidget(self.CentralWidget)
        QtCore.QMetaObject.connectSlotsByName(FinestraInserisciCliente)

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
    try:
        app = QtWidgets.QApplication(sys.argv)
        FinestraInserisciCliente = QtWidgets.QMainWindow()
        ui = Ui_FinestraInserisciCliente()
        ui.configurazioneInterfaccia(FinestraInserisciCliente)
        FinestraInserisciCliente.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Errore durante l'esecuzione dell'applicazione: {e}")
