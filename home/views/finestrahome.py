# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from home.views import img_rc  # Importa le risorse

class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path

class Ui_FinestraHome(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, FinestraHome):
        # Imposta il nome, la dimensione minima e massima della finestra
        FinestraHome.setObjectName("FinestraHome")
        FinestraHome.resize(761, 641)
        FinestraHome.setMinimumSize(QtCore.QSize(761, 641))
        FinestraHome.setMaximumSize(QtCore.QSize(761, 641))

        self.centralwidget = QtWidgets.QWidget(FinestraHome)
        self.centralwidget.setMinimumSize(QtCore.QSize(761, 641))
        self.centralwidget.setMaximumSize(QtCore.QSize(761, 641))
        self.centralwidget.setObjectName("centralwidget")

        # Creazione dello sfondo come primo elemento della centralwidget
        self.labelSfondoFinestraHome = QtWidgets.QLabel(self.centralwidget)
        self.labelSfondoFinestraHome.setGeometry(QtCore.QRect(0, 0, 761, 641))
        self.labelSfondoFinestraHome.setPixmap(QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg"))
        self.labelSfondoFinestraHome.setScaledContents(True)
        self.labelSfondoFinestraHome.setObjectName("labelSfondoFinestraHome")
        self.labelSfondoFinestraHome.lower()  # Imposta lo sfondo dietro gli altri widget

        # Barra alta
        self.BarraAlta = QtWidgets.QLabel(self.centralwidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 761, 41))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        # Altezza della barra alta
        barra_alta_height = 41  # Questo valore è l'altezza della BarraAlta

        # Pulsanti della finestra principale
        self.button_lista_clienti = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_clienti.setGeometry(QtCore.QRect(110, 130, 200, 100))
        self.button_lista_clienti.setStyleSheet(self.button_style())
        self.button_lista_clienti.setObjectName("button_lista_clienti")
        self.button_lista_clienti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button_lista_ordini = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_ordini.setGeometry(QtCore.QRect(440, 130, 200, 100))
        self.button_lista_ordini.setStyleSheet(self.button_style())
        self.button_lista_ordini.setObjectName("button_lista_ordini")
        self.button_lista_ordini.setFocusPolicy(QtCore.Qt.NoFocus)

        # Pulsanti aggiuntivi
        self.button_lista_dipendenti = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_dipendenti.setGeometry(QtCore.QRect(110, 250, 200, 100))
        self.button_lista_dipendenti.setStyleSheet(self.button_style())
        self.button_lista_dipendenti.setObjectName("button_lista_dipendenti")
        self.button_lista_dipendenti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button_lista_documenti = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_documenti.setGeometry(QtCore.QRect(440, 250, 200, 100))
        self.button_lista_documenti.setStyleSheet(self.button_style())
        self.button_lista_documenti.setObjectName("button_lista_documenti")
        self.button_lista_documenti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button_lista_fornitori = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_fornitori.setGeometry(QtCore.QRect(110, 370, 200, 100))
        self.button_lista_fornitori.setStyleSheet(self.button_style())
        self.button_lista_fornitori.setObjectName("button_lista_fornitori")
        self.button_lista_fornitori.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button_lista_enti_esterni = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_enti_esterni.setGeometry(QtCore.QRect(440, 370, 200, 100))
        self.button_lista_enti_esterni.setStyleSheet(self.button_style())
        self.button_lista_enti_esterni.setObjectName("button_lista_enti_esterni")
        self.button_lista_enti_esterni.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button_lista_prodotti = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_prodotti.setGeometry(QtCore.QRect(110, 490, 200, 100))
        self.button_lista_prodotti.setStyleSheet(self.button_style())
        self.button_lista_prodotti.setObjectName("button_lista_prodotti")
        self.button_lista_prodotti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button_lista_macchine = QtWidgets.QPushButton(self.centralwidget)
        self.button_lista_macchine.setGeometry(QtCore.QRect(440, 490, 200, 100))
        self.button_lista_macchine.setStyleSheet(self.button_style())
        self.button_lista_macchine.setObjectName("button_lista_macchine")
        self.button_lista_macchine.setFocusPolicy(QtCore.Qt.NoFocus)

        # Pulsante invisibile per evitare il focus sui pulsanti visibili
        self.hidden_focus_widget = QtWidgets.QWidget(self.centralwidget)
        self.hidden_focus_widget.setGeometry(QtCore.QRect(-10, -10, 1, 1))  # Posizionato fuori dalla vista
        self.hidden_focus_widget.setFocus()  # Imposta il focus su questo widget invisibile

        # Data e Ora
        self.lblDataTime = QtWidgets.QDateEdit(self.centralwidget)
        self.lblDataTime.setGeometry(QtCore.QRect(10, (barra_alta_height - 30) // 2, 100, 30))  # Centra verticalmente
        self.lblDataTime.setStyleSheet(self.date_edit_style())
        self.lblDataTime.setDateTime(QtCore.QDateTime.currentDateTime())
        self.lblDataTime.setObjectName("lblDataTime")

        # Creazione e configurazione della label "Home" al centro della barra alta
        self.labelHome = QtWidgets.QLabel(self.centralwidget)
        self.labelHome.setGeometry(QtCore.QRect(0, 0, 761, 41))  # Larghezza totale della barra alta
        self.labelHome.setStyleSheet(self.label_style())  # Applica lo stile esattamente come nel file .ui
        self.labelHome.setText("Home")
        self.labelHome.setObjectName("labelHome")

        # Centra il testo all'interno della QLabel
        self.labelHome.setAlignment(QtCore.Qt.AlignCenter)  # Allinea il testo al centro

        # Definire la larghezza delle icone
        icon_width = 24
        # Definire la distanza desiderata tra le icone
        spacing = 10

        # Ricrea le icone con questa nuova dimensione
        start_x = 761 - (3 * icon_width + 2 * spacing) - 10

        # Icona "Menu" (9042808_menu_icon.svg) - Prima da destra
        self.svg_icon_tendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.centralwidget)
        self.svg_icon_tendina.setGeometry(QtCore.QRect(start_x + 2 * (icon_width + spacing), 10, icon_width, icon_width))
        self.svg_icon_tendina.setObjectName("svg_icon_tendina")
        self.svg_icon_tendina.show()

        # Icona "Utente Connesso" (9042880_profile_circled_icon.svg) - Al centro
        self.svg_icon_utente = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg", self.centralwidget)
        self.svg_icon_utente.setGeometry(QtCore.QRect(start_x + icon_width + spacing, 10, icon_width, icon_width))
        self.svg_icon_utente.setObjectName("svg_icon_utente")
        self.svg_icon_utente.show()

        # Icona "Info Software" (9042463_language_icon.svg) - Ultima a sinistra
        self.svg_icon_info_software = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.centralwidget)
        self.svg_icon_info_software.setGeometry(QtCore.QRect(start_x, 10, icon_width, icon_width))
        self.svg_icon_info_software.setObjectName("svg_icon_info_software")
        self.svg_icon_info_software.show()

        FinestraHome.setCentralWidget(self.centralwidget)
        self.retranslateUi(FinestraHome)
        QtCore.QMetaObject.connectSlotsByName(FinestraHome)

    def retranslateUi(self, FinestraHome):
        _translate = QtCore.QCoreApplication.translate
        FinestraHome.setWindowTitle(_translate("FinestraHome", "Home"))
        self.button_lista_clienti.setText(_translate("FinestraHome", "Clienti"))
        self.button_lista_ordini.setText(_translate("FinestraHome", "Ordini"))
        self.button_lista_dipendenti.setText(_translate("FinestraHome", "Dipendenti"))
        self.button_lista_documenti.setText(_translate("FinestraHome", "Documenti"))
        self.button_lista_fornitori.setText(_translate("FinestraHome", "Fornitori"))
        self.button_lista_enti_esterni.setText(_translate("FinestraHome", "Enti Esterni"))
        self.button_lista_prodotti.setText(_translate("FinestraHome", "Prodotti"))
        self.button_lista_macchine.setText(_translate("FinestraHome", "Macchine"))

    #Stile del titolo Home
    def label_style(self):
        return """
        QLabel {
            font-family: "Verdana", sans-serif;  /* Font informatico discreto */
            font-size: 24px;  /* Dimensione del testo */
            color: #FFFFFF;  /* Colore bianco */
            font-weight: normal;  /* Normale, senza grassetto */
        }
        """

    # Stile dei pulsanti
    def button_style(self):
        return """
        QPushButton {
            background-color: #283747;
            border-radius: 8px;
            border: 3px solid #FFFFFF;
            color: #FFFFFF;  /* Colore del testo bianco permanente */
            font-size: 20px;
            font-weight: 500;
            transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out;
        }
        QPushButton:hover {
            background-color: #1E2230;  /* Colore di sfondo più scuro al passaggio del mouse */
            border-color: #FFFFFF;  /* Mantiene il bordo bianco */
            /* Colore del testo non cambiato qui, resta bianco */
        }
        QPushButton:pressed {
            background-color: #333944;  /* Colore del pulsante quando viene premuto */
            border-color: #CCCCCC;
            /* Il testo resta bianco */
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