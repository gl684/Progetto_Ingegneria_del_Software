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
        self.configurazioneInterfaccia(self)

    def configurazioneInterfaccia(self, FinestraHome):
        # Imposta il nome, la dimensione minima e massima della finestra
        FinestraHome.setObjectName("FinestraHome")
        FinestraHome.resize(761, 641)
        FinestraHome.setMinimumSize(QtCore.QSize(761, 641))
        FinestraHome.setMaximumSize(QtCore.QSize(761, 641))

        self.CentralWidget = QtWidgets.QWidget(FinestraHome)
        self.CentralWidget.setMinimumSize(QtCore.QSize(761, 641))
        self.CentralWidget.setMaximumSize(QtCore.QSize(761, 641))
        self.CentralWidget.setObjectName("CentralWidget")

        # Creazione dello sfondo come primo elemento della CentralWidget
        self.LabelSfondoFinestraHome = QtWidgets.QLabel(self.CentralWidget)
        self.LabelSfondoFinestraHome.setGeometry(QtCore.QRect(0, 0, 761, 641))
        self.LabelSfondoFinestraHome.setPixmap(QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg"))
        self.LabelSfondoFinestraHome.setScaledContents(True)
        self.LabelSfondoFinestraHome.setObjectName("LabelSfondoFinestraHome")
        self.LabelSfondoFinestraHome.lower()  # Imposta lo sfondo dietro gli altri widget

        # Barra alta
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 761, 41))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        # Altezza della barra alta
        AltezzaBarraAlta = 41  # Questo valore è l'altezza della BarraAlta

        # Pulsanti della finestra principale
        self.ButtonListaClienti = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaClienti.setGeometry(QtCore.QRect(110, 130, 200, 100))
        self.ButtonListaClienti.setStyleSheet(self.stileButton())
        self.ButtonListaClienti.setObjectName("ButtonListaClienti")
        self.ButtonListaClienti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ButtonListaOrdini = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaOrdini.setGeometry(QtCore.QRect(440, 130, 200, 100))
        self.ButtonListaOrdini.setStyleSheet(self.stileButton())
        self.ButtonListaOrdini.setObjectName("ButtonListaOrdini")
        self.ButtonListaOrdini.setFocusPolicy(QtCore.Qt.NoFocus)

        # Pulsanti aggiuntivi
        self.ButtonListaDipendenti = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaDipendenti.setGeometry(QtCore.QRect(110, 250, 200, 100))
        self.ButtonListaDipendenti.setStyleSheet(self.stileButton())
        self.ButtonListaDipendenti.setObjectName("ButtonListaDipendenti")
        self.ButtonListaDipendenti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ButtonListaDocumenti = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaDocumenti.setGeometry(QtCore.QRect(440, 250, 200, 100))
        self.ButtonListaDocumenti.setStyleSheet(self.stileButton())
        self.ButtonListaDocumenti.setObjectName("ButtonListaDocumenti")
        self.ButtonListaDocumenti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ButtonListaFornitori = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaFornitori.setGeometry(QtCore.QRect(110, 370, 200, 100))
        self.ButtonListaFornitori.setStyleSheet(self.stileButton())
        self.ButtonListaFornitori.setObjectName("ButtonListaFornitori")
        self.ButtonListaFornitori.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ButtonListaEntiEsterni = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaEntiEsterni.setGeometry(QtCore.QRect(440, 370, 200, 100))
        self.ButtonListaEntiEsterni.setStyleSheet(self.stileButton())
        self.ButtonListaEntiEsterni.setObjectName("ButtonListaEntiEsterni")
        self.ButtonListaEntiEsterni.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ButtonListaProdotti = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaProdotti.setGeometry(QtCore.QRect(110, 490, 200, 100))
        self.ButtonListaProdotti.setStyleSheet(self.stileButton())
        self.ButtonListaProdotti.setObjectName("ButtonListaProdotti")
        self.ButtonListaProdotti.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ButtonListaMacchine = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonListaMacchine.setGeometry(QtCore.QRect(440, 490, 200, 100))
        self.ButtonListaMacchine.setStyleSheet(self.stileButton())
        self.ButtonListaMacchine.setObjectName("ButtonListaMacchine")
        self.ButtonListaMacchine.setFocusPolicy(QtCore.Qt.NoFocus)

        # Pulsante invisibile per evitare il focus sui pulsanti visibili
        self.HiddenFocusWidget = QtWidgets.QWidget(self.CentralWidget)
        self.HiddenFocusWidget.setGeometry(QtCore.QRect(-10, -10, 1, 1))  # Posizionato fuori dalla vista
        self.HiddenFocusWidget.setFocus()  # Imposta il focus su questo widget invisibile

        # Data e Ora
        self.LabelDataTime = QtWidgets.QDateEdit(self.CentralWidget)
        self.LabelDataTime.setGeometry(QtCore.QRect(10, (AltezzaBarraAlta - 30) // 2, 100, 30))  # Centra verticalmente
        self.LabelDataTime.setStyleSheet(self.stileData())
        self.LabelDataTime.setDateTime(QtCore.QDateTime.currentDateTime())
        self.LabelDataTime.setObjectName("LabelDataTime")

        # Creazione e configurazione della label "Home" al centro della barra alta
        self.LabelHome = QtWidgets.QLabel(self.CentralWidget)
        self.LabelHome.setGeometry(QtCore.QRect(0, 0, 761, 41))  # Larghezza totale della barra alta
        self.LabelHome.setStyleSheet(self.stileLabel())  # Applica lo stile esattamente come nel file .ui
        self.LabelHome.setText("Home")
        self.LabelHome.setObjectName("LabelHome")

        # Centra il testo all'interno della QLabel
        self.LabelHome.setAlignment(QtCore.Qt.AlignCenter)  # Allinea il testo al centro

        # Definire la larghezza delle icone
        larghezzaIcona = 24
        # Definire la distanza desiderata tra le icone
        spaziatura = 10
        # Ricrea le icone con questa nuova dimensione
        inizioX = 761 - (3 * larghezzaIcona + 2 * spaziatura) - 10

        # Icona "Menu" (9042808_menu_icon.svg) - Prima da destra
        self.SvgIconTendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.CentralWidget)
        self.SvgIconTendina.setGeometry(QtCore.QRect(inizioX + 2 * (larghezzaIcona + spaziatura), 10, larghezzaIcona, larghezzaIcona))
        self.SvgIconTendina.setObjectName("SvgIconTendina")
        self.SvgIconTendina.show()

        # Icona "Utente Connesso" (9042880_profile_circled_icon.svg) - Al centro
        self.SvgIconUtente = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg", self.CentralWidget)
        self.SvgIconUtente.setGeometry(QtCore.QRect(inizioX + larghezzaIcona + spaziatura, 10, larghezzaIcona, larghezzaIcona))
        self.SvgIconUtente.setObjectName("SvgIconUtente")
        self.SvgIconUtente.show()

        # Icona "Info Software" (9042463_language_icon.svg) - Ultima a sinistra
        self.SvgIconInfoSoftware = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.CentralWidget)
        self.SvgIconInfoSoftware.setGeometry(QtCore.QRect(inizioX, 10, larghezzaIcona, larghezzaIcona))
        self.SvgIconInfoSoftware.setObjectName("SvgIconInfoSoftware")
        self.SvgIconInfoSoftware.show()

        FinestraHome.setCentralWidget(self.CentralWidget)
        self.aggiornaTestiInterfaccia(FinestraHome)
        QtCore.QMetaObject.connectSlotsByName(FinestraHome)

    def aggiornaTestiInterfaccia(self, FinestraHome):
        trad = QtCore.QCoreApplication.translate
        FinestraHome.setWindowTitle(trad("FinestraHome", "Home"))
        self.ButtonListaClienti.setText(trad("FinestraHome", "Clienti"))
        self.ButtonListaOrdini.setText(trad("FinestraHome", "Ordini"))
        self.ButtonListaDipendenti.setText(trad("FinestraHome", "Dipendenti"))
        self.ButtonListaDocumenti.setText(trad("FinestraHome", "Documenti"))
        self.ButtonListaFornitori.setText(trad("FinestraHome", "Fornitori"))
        self.ButtonListaEntiEsterni.setText(trad("FinestraHome", "Enti Esterni"))
        self.ButtonListaProdotti.setText(trad("FinestraHome", "Prodotti"))
        self.ButtonListaMacchine.setText(trad("FinestraHome", "Macchine"))

    # Stile del titolo Home
    def stileLabel(self):
        return """
        QLabel {
            font-family: "Verdana", sans-serif;  /* Font informatico discreto */
            font-size: 24px;  /* Dimensione del testo */
            color: #FFFFFF;  /* Colore bianco */
            font-weight: normal;  /* Normale, senza grassetto */
        }
        """

    # Stile dei pulsanti
    def stileButton(self):
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
