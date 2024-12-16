# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui, QtSvg


class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path


class Ui_FinestraModificaCliente(object):
    def configurazioneInterfaccia(self, FinestraModificaCliente):
        FinestraModificaCliente.setObjectName("FinestraModificaCliente")
        FinestraModificaCliente.resize(700, 600)
        FinestraModificaCliente.setFixedSize(700, 600)

        # Widget principale
        self.CentralWidget = QtWidgets.QWidget(FinestraModificaCliente)
        self.CentralWidget.setObjectName("centralWidget")
        FinestraModificaCliente.setCentralWidget(self.CentralWidget)  # Imposta il widget centrale

        # Sfondo con QLabel
        self.label = QtWidgets.QLabel(self.CentralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 600))
        self.label.setPixmap(QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg").scaled(
            700, 600, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation
        ))
        self.label.setScaledContents(False)  # Evita ulteriori ridimensionamenti dinamici
        self.label.setObjectName("label")

        # Barra Alta
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 700, 41))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        self.BarraAlta.setText("")
        self.BarraAlta.setObjectName("BarraAlta")

        # Label Modifica Cliente
        self.labelModificaCliente = QtWidgets.QLabel(self.CentralWidget)
        self.labelModificaCliente.setGeometry(QtCore.QRect(280, 10, 171, 20))
        self.labelModificaCliente.setStyleSheet(
            "font-family: 'Verdana'; font-size: 20px; color: white; font-weight: normal")
        self.labelModificaCliente.setObjectName("labelModificaCliente")

        # **Nuova Label Tipo Cliente** - sottostante alla barra alta
        self.labelTipoCliente = QtWidgets.QLabel(self.CentralWidget)
        self.labelTipoCliente.setGeometry(QtCore.QRect(70, 60, 171, 20))
        self.labelTipoCliente.setStyleSheet(
            "font-family: 'Verdana'; font-size: 15px; color: #283747; font-weight: bold")
        self.labelTipoCliente.setObjectName("labelTipoCliente")

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
        inizioX = 670
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

        # StackedWidget con layout
        self.stackedWidget = QtWidgets.QStackedWidget(self.CentralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(60, 100, 580, 200))
        self.stackedWidget.setStyleSheet(self.stileStackedWidget())
        self.stackedWidget.setObjectName("stackedWidget")

        # Pagina Cliente Privato
        self.ClientePrivato = QtWidgets.QWidget()
        self.ClientePrivato.setObjectName("ClientePrivato")

        privatoLayout = QtWidgets.QFormLayout(self.ClientePrivato)
        self.labelNome = QtWidgets.QLabel("Nome:", self.ClientePrivato)
        self.labelNome.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditNome = QtWidgets.QLineEdit(self.ClientePrivato)
        privatoLayout.addRow(self.labelNome, self.lineEditNome)

        self.labelCognome = QtWidgets.QLabel("Cognome:", self.ClientePrivato)
        self.labelCognome.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditCognome = QtWidgets.QLineEdit(self.ClientePrivato)
        privatoLayout.addRow(self.labelCognome, self.lineEditCognome)

        self.labelCF = QtWidgets.QLabel("Codice Fiscale:", self.ClientePrivato)
        self.labelCF.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditCF = QtWidgets.QLineEdit(self.ClientePrivato)
        privatoLayout.addRow(self.labelCF, self.lineEditCF)

        self.stackedWidget.addWidget(self.ClientePrivato)

        # Pagina Cliente Azienda
        self.ClienteAzienda = QtWidgets.QWidget()
        self.ClienteAzienda.setObjectName("ClienteAzienda")

        aziendaLayout = QtWidgets.QFormLayout(self.ClienteAzienda)
        self.labelNomeAzienda = QtWidgets.QLabel("Nome Azienda:", self.ClienteAzienda)
        self.labelNomeAzienda.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditNomeAzienda = QtWidgets.QLineEdit(self.ClienteAzienda)
        aziendaLayout.addRow(self.labelNomeAzienda, self.lineEditNomeAzienda)

        self.labelPartitaIVA = QtWidgets.QLabel("Partita IVA:", self.ClienteAzienda)
        self.labelPartitaIVA.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditPartitaIVA = QtWidgets.QLineEdit(self.ClienteAzienda)
        aziendaLayout.addRow(self.labelPartitaIVA, self.lineEditPartitaIVA)

        self.stackedWidget.addWidget(self.ClienteAzienda)

        # Campi comuni
        commonLayout = QtWidgets.QFormLayout()
        self.labelEmail = QtWidgets.QLabel("Email:", self.CentralWidget)
        self.labelEmail.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditEmail = QtWidgets.QLineEdit(self.CentralWidget)
        commonLayout.addRow(self.labelEmail, self.lineEditEmail)

        self.labelTelefono = QtWidgets.QLabel("Telefono:", self.CentralWidget)
        self.labelTelefono.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditTelefono = QtWidgets.QLineEdit(self.CentralWidget)
        commonLayout.addRow(self.labelTelefono, self.lineEditTelefono)

        self.labelIndirizzo = QtWidgets.QLabel("Indirizzo:", self.CentralWidget)
        self.labelIndirizzo.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.lineEditIndirizzo = QtWidgets.QLineEdit(self.CentralWidget)
        commonLayout.addRow(self.labelIndirizzo, self.lineEditIndirizzo)

        commonWidget = QtWidgets.QWidget(self.CentralWidget)
        commonWidget.setGeometry(QtCore.QRect(60, 310, 580, 150))
        commonWidget.setLayout(commonLayout)

        # **Pulsanti**
        self.ButtonSalvaModifica = QtWidgets.QPushButton("Salva", self.CentralWidget)
        self.ButtonSalvaModifica.setGeometry(QtCore.QRect(250, 460, 181, 71))
        self.ButtonSalvaModifica.setStyleSheet(self.stileButton())
        self.ButtonSalvaModifica.setObjectName("ButtonSalvaModifica")

        self.ButtonAnnullaModifica = QtWidgets.QPushButton("Annulla", self.CentralWidget)
        self.ButtonAnnullaModifica.setGeometry(
            QtCore.QRect(250, 520, 181, 71))
        self.ButtonAnnullaModifica.setStyleSheet(self.stileButton())
        self.ButtonAnnullaModifica.setObjectName("ButtonAnnullaModifica")

        self.aggiornaTestiInterfaccia(FinestraModificaCliente)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FinestraModificaCliente)

    def setTipoCliente(self, is_privato):
        if is_privato:
            tipo_cliente = "Cliente Privato"
        else:
            tipo_cliente = "Cliente Azienda"
        self.labelTipoCliente.setText(tipo_cliente)

    def aggiornaTestiInterfaccia(self, FinestraModificaCliente):
        trad = QtCore.QCoreApplication.translate
        FinestraModificaCliente.setWindowTitle(trad("FinestraModificaCliente", "Modifica Cliente"))
        self.labelModificaCliente.setText(trad("FinestraModificaCliente", "Modifica Cliente"))


        if self.stackedWidget.currentIndex() == 0:
            tipo_cliente = "Cliente Privato"
        else:
            tipo_cliente = "Cliente Azienda"

        self.labelTipoCliente.setText(trad("FinestraModificaCliente", tipo_cliente))

        # Pagina Cliente Privato
        self.labelNome.setText(trad("FinestraModificaCliente", "Nome:"))
        self.labelCognome.setText(trad("FinestraModificaCliente", "Cognome:"))
        self.labelCF.setText(trad("FinestraModificaCliente", "Codice Fiscale:"))

        # Pagina Cliente Azienda
        self.labelNomeAzienda.setText(trad("FinestraModificaCliente", "Nome Azienda:"))
        self.labelPartitaIVA.setText(trad("FinestraModificaCliente", "Partita IVA:"))

        # Campi Comuni
        self.labelEmail.setText(trad("FinestraModificaCliente", "Email:"))
        self.labelTelefono.setText(trad("FinestraModificaCliente", "Telefono:"))
        self.labelIndirizzo.setText(trad("FinestraModificaCliente", "Indirizzo:"))

        self.ButtonSalvaModifica.setText(trad("FinestraModificaCliente", "Salva"))
        self.ButtonAnnullaModifica.setText(trad("FinestraModificaCliente", "Annulla"))

    def stileStackedWidget(self):
        return """
        QStackedWidget {
            background-color: transparent; /* Trasparente */
            border: 1px solid #b0b0b0; /* Bordo grigio chiaro */
            border-radius: 10px; /* Angoli arrotondati */
            margin: 10px; /* Spazio esterno */
            padding: 5px; /* Margine interno */
        }
        """

    def stileButton(self):
        return """
            QPushButton {
                background-color: #283747;
                border-radius: 8px;
                border: 3px solid #FFFFFF; /* Bordo bianco esterno */
                box-sizing: border-box;
                color: #FFFFFF;
                padding: 8px;
                text-align: center;
                display: inline-block;
                font-size: 17px;
                font-weight: 500;
                line-height: 1;
                margin: 10px 2px;
                cursor: pointer;
                transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
            }

            QPushButton:hover {
                background-color: #1E2230;
                border-color: #FFFFFF; /* Mantieni il bordo bianco al passaggio del mouse */
            }

            QPushButton:focus {
                background-color: #242835;
                border-color: #FFFFFF; /* Mantieni il bordo bianco al focus */
                box-shadow: rgba(255, 255, 255, 0.15) 0 1px 0 inset, rgba(46, 54, 80, 0.075) 0 1px 1px, rgba(104, 101, 235, 0.5) 0 0 0 32px;
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
    FinestraModificaCliente = QtWidgets.QMainWindow()
    ui = Ui_FinestraModificaCliente()
    ui.configurazioneInterfaccia(FinestraModificaCliente)
    FinestraModificaCliente.show()
    sys.exit(app.exec_())
