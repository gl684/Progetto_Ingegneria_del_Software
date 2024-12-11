from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from PyQt5.QtGui import QPixmap


class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path

class Ui_FinestraInserisciCliente(object):
    def setupUi(self, FinestraInserisciCliente):
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
        self.label.setScaledContents(True)
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
        self.lblDataTime = QtWidgets.QDateEdit(self.CentralWidget)
        self.lblDataTime.setGeometry(QtCore.QRect(10, 5, 100, 30))  # Posizionamento corretto
        self.lblDataTime.setStyleSheet(self.date_edit_style())
        self.lblDataTime.setDate(QtCore.QDate.currentDate())
        self.lblDataTime.setDisplayFormat("dd/MM/yyyy")
        self.lblDataTime.setCalendarPopup(True)
        self.lblDataTime.setObjectName("lblDataTime")

        # Definizione dimensioni e posizione delle icone
        icon_width = 20
        spacing = 8
        start_x = 530
        barra_alta_height = 41  # Altezza della barra
        vertical_center = (barra_alta_height - icon_width) // 2  # Calcola il centro verticale

        # Icona Menu Tendina
        self.ButtonTendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.CentralWidget)
        self.ButtonTendina.setGeometry(QtCore.QRect(start_x, vertical_center, icon_width, icon_width))
        self.ButtonTendina.setObjectName("ButtonTendina")

        # Icona Utente Connesso
        self.ButtonUtenteConnesso = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg",
                                            self.CentralWidget)
        self.ButtonUtenteConnesso.setGeometry(
            QtCore.QRect(start_x - icon_width - spacing, vertical_center, icon_width, icon_width))
        self.ButtonUtenteConnesso.setObjectName("ButtonUtenteConnesso")

        # Icona Info Software
        self.ButtonInfoSoftware = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.CentralWidget)
        self.ButtonInfoSoftware.setGeometry(
            QtCore.QRect(start_x - 2 * (icon_width + spacing), vertical_center, icon_width, icon_width))
        self.ButtonInfoSoftware.setObjectName("ButtonInfoSoftware")

        # **Tipo Cliente**
        self.label_tipo_cliente = QtWidgets.QLabel(self.CentralWidget)
        self.label_tipo_cliente.setGeometry(QtCore.QRect(40, 80, 73, 22))
        self.label_tipo_cliente.setText("Tipo Cliente:")
        self.comboBox_tipo_cliente = QtWidgets.QComboBox(self.CentralWidget)
        self.comboBox_tipo_cliente.setGeometry(QtCore.QRect(130, 80, 296, 22))
        self.comboBox_tipo_cliente.addItems(["Privato", "Azienda"])

        # **Campi Comuni**
        self.label_indirizzo = QtWidgets.QLabel(self.CentralWidget)
        self.label_indirizzo.setGeometry(QtCore.QRect(40, 200, 73, 22))
        self.label_indirizzo.setText("Indirizzo:")
        self.lineEdit_indirizzo = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_indirizzo.setGeometry(QtCore.QRect(130, 200, 296, 22))

        self.label_telefono = QtWidgets.QLabel(self.CentralWidget)
        self.label_telefono.setGeometry(QtCore.QRect(40, 240, 73, 22))
        self.label_telefono.setText("Telefono:")
        self.lineEdit_telefono = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_telefono.setGeometry(QtCore.QRect(130, 240, 296, 22))

        self.label_email = QtWidgets.QLabel(self.CentralWidget)
        self.label_email.setGeometry(QtCore.QRect(40, 280, 73, 22))
        self.label_email.setText("Email:")
        self.lineEdit_email = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(130, 280, 296, 22))

        # **Campi Cliente Privato**
        self.label_nome = QtWidgets.QLabel(self.CentralWidget)
        self.label_nome.setGeometry(QtCore.QRect(40, 320, 73, 22))
        self.label_nome.setText("Nome:")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(130, 320, 296, 22))

        self.label_cognome = QtWidgets.QLabel(self.CentralWidget)
        self.label_cognome.setGeometry(QtCore.QRect(40, 360, 73, 22))
        self.label_cognome.setText("Cognome:")
        self.lineEdit_cognome = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_cognome.setGeometry(QtCore.QRect(130, 360, 296, 22))

        self.label_codice_fiscale = QtWidgets.QLabel(self.CentralWidget)
        self.label_codice_fiscale.setGeometry(QtCore.QRect(40, 400, 100, 22))
        self.label_codice_fiscale.setText("Codice Fiscale:")
        self.lineEdit_codice_fiscale = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_codice_fiscale.setGeometry(QtCore.QRect(130, 400, 296, 22))

        # **Campi Cliente Azienda**
        self.label_nome_azienda = QtWidgets.QLabel(self.CentralWidget)
        self.label_nome_azienda.setGeometry(QtCore.QRect(40, 320, 100, 22))
        self.label_nome_azienda.setText("Nome Azienda:")
        self.lineEdit_nome_azienda = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_nome_azienda.setGeometry(QtCore.QRect(130, 320, 296, 22))

        self.label_partita_iva = QtWidgets.QLabel(self.CentralWidget)
        self.label_partita_iva.setGeometry(QtCore.QRect(40, 360, 100, 22))
        self.label_partita_iva.setText("Partita IVA:")
        self.lineEdit_partita_iva = QtWidgets.QLineEdit(self.CentralWidget)
        self.lineEdit_partita_iva.setGeometry(QtCore.QRect(130, 360, 296, 22))

        # **Bottoni**
        self.ButtonConferma = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonConferma.setGeometry(QtCore.QRect(90, 460, 171, 50))  # Posizionato più in basso
        self.ButtonConferma.setStyleSheet(self.button_style())  # Applica lo stile
        self.ButtonConferma.setText("Conferma")

        self.ButtonAnnulla = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonAnnulla.setGeometry(QtCore.QRect(300, 460, 171, 50))  # Posizionato più in basso
        self.ButtonAnnulla.setStyleSheet(self.button_style())  # Applica lo stile
        self.ButtonAnnulla.setText("Annulla")

        # **Logica di Default**
        self.label_nome.hide()
        self.lineEdit_nome.hide()
        self.label_cognome.hide()
        self.lineEdit_cognome.hide()
        self.label_codice_fiscale.hide()
        self.lineEdit_codice_fiscale.hide()

        self.label_nome_azienda.hide()
        self.lineEdit_nome_azienda.hide()
        self.label_partita_iva.hide()
        self.lineEdit_partita_iva.hide()

        FinestraInserisciCliente.setCentralWidget(self.CentralWidget)
        QtCore.QMetaObject.connectSlotsByName(FinestraInserisciCliente)

    def button_style(self):
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
    def date_edit_style(self):
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
        ui.setupUi(FinestraInserisciCliente)
        FinestraInserisciCliente.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Errore durante l'esecuzione dell'applicazione: {e}")
