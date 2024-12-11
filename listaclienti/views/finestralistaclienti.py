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
    def setupUi(self, FinestraListaClienti):
        FinestraListaClienti.setObjectName("FinestraListaClienti")
        FinestraListaClienti.resize(661, 521)
        FinestraListaClienti.setFixedSize(661, 521)

        self.CentralWidget = QtWidgets.QWidget(FinestraListaClienti)
        self.CentralWidget.setObjectName("CentralWidget")

        # Sfondo
        self.LabelSfondo = QtWidgets.QLabel(self.CentralWidget)
        self.LabelSfondo.setGeometry(QtCore.QRect(0, 0, 661, 521))
        self.LabelSfondo.setPixmap(QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg"))
        self.LabelSfondo.setScaledContents(True)
        self.LabelSfondo.setObjectName("LabelSfondo")

        # Barra superiore
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 661, 41))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        self.BarraAlta.setObjectName("BarraAlta")

        # Titolo
        self.LabelTitolo = QtWidgets.QLabel(self.CentralWidget)
        self.LabelTitolo.setGeometry(QtCore.QRect(290, 10, 91, 20))
        self.LabelTitolo.setStyleSheet("color: white; font-family: Verdana; font-size: 24px;")
        self.LabelTitolo.setObjectName("LabelTitolo")

        # Pulsante Apri
        self.ButtonApriCliente = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonApriCliente.setGeometry(QtCore.QRect(470, 80, 141, 61))
        self.ButtonApriCliente.setStyleSheet(self.button_style())
        self.ButtonApriCliente.setObjectName("ButtonApriCliente")
        self.ButtonApriCliente.setFocusPolicy(QtCore.Qt.NoFocus)

        # Pulsante Nuovo
        self.ButtonAggiungiCliente = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonAggiungiCliente.setGeometry(QtCore.QRect(470, 160, 141, 61))
        self.ButtonAggiungiCliente.setStyleSheet(self.button_style())
        self.ButtonAggiungiCliente.setObjectName("ButtonAggiungiCliente")
        self.ButtonAggiungiCliente.setFocusPolicy(QtCore.Qt.NoFocus)

        # Pulsante invisibile per evitare il focus sui pulsanti visibili
        self.HiddenFocusWidget = QtWidgets.QWidget(self.CentralWidget)
        self.HiddenFocusWidget.setGeometry(QtCore.QRect(-10, -10, 1, 1))  # Posizionato fuori dalla vista
        self.HiddenFocusWidget.setFocus()  # Imposta il focus su questo widget invisibile

        # Lista Clienti
        self.ListaClienti = QtWidgets.QListWidget(self.CentralWidget)
        self.ListaClienti.setGeometry(QtCore.QRect(30, 60, 421, 431))
        self.ListaClienti.setObjectName("ListaClienti")

        # Data
        self.LabelDataTime = QtWidgets.QDateEdit(self.CentralWidget)
        self.LabelDataTime.setGeometry(QtCore.QRect(10, 5, 100, 30))  # Posizionamento corretto
        self.LabelDataTime.setStyleSheet(self.date_edit_style())
        self.LabelDataTime.setDate(QtCore.QDate.currentDate())
        self.LabelDataTime.setDisplayFormat("dd/MM/yyyy")
        self.LabelDataTime.setCalendarPopup(True)
        self.LabelDataTime.setObjectName("LabelDataTime")

        # Definizione dimensioni e posizione delle icone
        icon_width = 24
        spacing = 10
        start_x = 630
        barra_alta_height = 41  # Altezza della barra
        vertical_center = (barra_alta_height - icon_width) // 2  # Calcola il centro verticale

        # Icona Menu Tendina
        self.ButtonTendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.CentralWidget)
        self.ButtonTendina.setGeometry(QtCore.QRect(start_x, vertical_center, icon_width, icon_width))
        self.ButtonTendina.setObjectName("ButtonTendina")

        # Icona Utente Connesso
        self.ButtonUtenteConnesso = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg", self.CentralWidget)
        self.ButtonUtenteConnesso.setGeometry(QtCore.QRect(start_x - icon_width - spacing, vertical_center, icon_width, icon_width))
        self.ButtonUtenteConnesso.setObjectName("ButtonUtenteConnesso")

        # Icona Info Software
        self.ButtonInfoSoftware = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.CentralWidget)
        self.ButtonInfoSoftware.setGeometry(QtCore.QRect(start_x - 2 * (icon_width + spacing), vertical_center, icon_width, icon_width))
        self.ButtonInfoSoftware.setObjectName("ButtonInfoSoftware")

        FinestraListaClienti.setCentralWidget(self.CentralWidget)
        self.retranslateUi(FinestraListaClienti)
        QtCore.QMetaObject.connectSlotsByName(FinestraListaClienti)

    def retranslateUi(self, FinestraListaClienti):
        _translate = QtCore.QCoreApplication.translate
        FinestraListaClienti.setWindowTitle(_translate("FinestraListaClienti", "MainWindow"))
        self.LabelTitolo.setText(_translate("FinestraListaClienti", "Clienti"))
        self.ButtonApriCliente.setText(_translate("FinestraListaClienti", "Apri"))
        self.ButtonAggiungiCliente.setText(_translate("FinestraListaClienti", "Nuovo"))

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
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_FinestraListaClienti()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
