# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from listaclienti.views import img_rc

# Classe per caricare e gestire icone SVG
class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path

class Ui_FinestraListaClienti:
    def configurazioneInterfaccia(self, FinestraListaClienti):
        FinestraListaClienti.setObjectName("FinestraListaClienti")
        FinestraListaClienti.resize(661, 521)
        FinestraListaClienti.setFixedSize(661, 521)

        self.CentralWidget = QtWidgets.QWidget(FinestraListaClienti)
        self.CentralWidget.setObjectName("CentralWidget")

        #Sfondo
        self.LabelSfondo = QtWidgets.QLabel(self.CentralWidget)
        self.LabelSfondo.setGeometry(QtCore.QRect(0, 0, 661, 521))
        self.LabelSfondo.setPixmap(QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg"))
        self.LabelSfondo.setScaledContents(True)
        self.LabelSfondo.setObjectName("LabelSfondo")

        #Barra in alto
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 661, 41))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        self.BarraAlta.setObjectName("BarraAlta")

        #Titolo
        self.LabelTitolo = QtWidgets.QLabel(self.CentralWidget)
        self.LabelTitolo.setGeometry(QtCore.QRect(290, 10, 91, 20))
        self.LabelTitolo.setStyleSheet("color: white; font-family: Verdana; font-size: 24px;")
        self.LabelTitolo.setObjectName("LabelTitolo")

        #Pulsante Apri
        self.ButtonApriCliente = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonApriCliente.setGeometry(QtCore.QRect(470, 80, 141, 61))
        self.ButtonApriCliente.setStyleSheet(self.stileButton())
        self.ButtonApriCliente.setObjectName("ButtonApriCliente")
        self.ButtonApriCliente.setFocusPolicy(QtCore.Qt.NoFocus)

        #Pulsante Nuovo
        self.ButtonAggiungiCliente = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonAggiungiCliente.setGeometry(QtCore.QRect(470, 160, 141, 61))
        self.ButtonAggiungiCliente.setStyleSheet(self.stileButton())
        self.ButtonAggiungiCliente.setObjectName("ButtonAggiungiCliente")
        self.ButtonAggiungiCliente.setFocusPolicy(QtCore.Qt.NoFocus)

        #Pulsante invisibile per evitare il focus sui pulsanti visibili
        self.HiddenFocusWidget = QtWidgets.QWidget(self.CentralWidget)
        self.HiddenFocusWidget.setGeometry(QtCore.QRect(-10, -10, 1, 1))  #Posizionato fuori dalla vista
        self.HiddenFocusWidget.setFocus()  #Imposta il focus su questo widget invisibile

        #Lista Clienti
        self.ListaClienti = QtWidgets.QListWidget(self.CentralWidget)
        self.ListaClienti.setGeometry(QtCore.QRect(30, 60, 421, 431))
        self.ListaClienti.setObjectName("ListaClienti")

        #Data
        self.LabelData = QtWidgets.QDateEdit(self.CentralWidget)
        self.LabelData.setGeometry(QtCore.QRect(10, 5, 100, 30))
        self.LabelData.setStyleSheet(self.stileData())
        self.LabelData.setDate(QtCore.QDate.currentDate())
        self.LabelData.setDisplayFormat("dd/MM/yyyy")
        self.LabelData.setCalendarPopup(True)
        self.LabelData.setObjectName("LabelDataTime")

        #Definizione dimensioni e posizione delle icone
        larghezzaIcona = 24
        spaziatura = 10
        inizioX = 630
        altezzaBarraAlta = 41  #Altezza della barra
        centroVerticale = (altezzaBarraAlta - larghezzaIcona) // 2  #Calcola il centro verticale

        #Icona Menu Tendina
        self.ButtonTendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.CentralWidget)
        self.ButtonTendina.setGeometry(QtCore.QRect(inizioX, centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonTendina.setObjectName("ButtonTendina")

        #Icona Utente Connesso
        self.ButtonUtenteConnesso = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg", self.CentralWidget)
        self.ButtonUtenteConnesso.setGeometry(QtCore.QRect(inizioX - larghezzaIcona - spaziatura, centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonUtenteConnesso.setObjectName("ButtonUtenteConnesso")

        #Icona Info Software
        self.ButtonInfoSoftware = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.CentralWidget)
        self.ButtonInfoSoftware.setGeometry(QtCore.QRect(inizioX - 2 * (larghezzaIcona + spaziatura), centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonInfoSoftware.setObjectName("ButtonInfoSoftware")

        FinestraListaClienti.setCentralWidget(self.CentralWidget)
        self.aggiornaTestiInterfaccia(FinestraListaClienti)
        QtCore.QMetaObject.connectSlotsByName(FinestraListaClienti)

    def aggiornaTestiInterfaccia(self, FinestraListaClienti):
        trad = QtCore.QCoreApplication.translate
        FinestraListaClienti.setWindowTitle(trad("FinestraListaClienti", "MainWindow"))
        self.LabelTitolo.setText(trad("FinestraListaClienti", "Clienti"))
        self.ButtonApriCliente.setText(trad("FinestraListaClienti", "Apri"))
        self.ButtonAggiungiCliente.setText(trad("FinestraListaClienti", "Nuovo"))

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
    app = QtWidgets.QApplication(sys.argv)
    FinestraListaClienti = QtWidgets.QMainWindow()
    ui = Ui_FinestraListaClienti()
    ui.configurazioneInterfaccia(FinestraListaClienti)
    FinestraListaClienti.show()
    sys.exit(app.exec_())
