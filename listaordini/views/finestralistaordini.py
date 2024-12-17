# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from cliente.views import img_rc


# Classe per caricare e gestire icone SVG
class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path


class Ui_FinestraListaOrdini:
    def configurazioneInterfaccia(self, FinestraListaOrdini):
        FinestraListaOrdini.setObjectName("FinestraListaOrdini")
        FinestraListaOrdini.resize(1014, 661)
        FinestraListaOrdini.setFixedSize(1014, 661)

        self.CentralWidget = QtWidgets.QWidget(FinestraListaOrdini)
        self.CentralWidget.setObjectName("centralwidget")

        #Sfondo
        self.LabelSfondo = QtWidgets.QLabel(self.CentralWidget)
        self.LabelSfondo.setGeometry(QtCore.QRect(0, 0, 1021, 661))
        self.LabelSfondo.setPixmap(QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg"))
        self.LabelSfondo.setScaledContents(True)
        self.LabelSfondo.setObjectName("LabelSfondo")

        #Barra in alto
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 1021, 51))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        self.BarraAlta.setObjectName("BarraAlta")

        #Titolo
        self.LabelTitolo = QtWidgets.QLabel(self.CentralWidget)
        self.LabelTitolo.setGeometry(QtCore.QRect(460, 10, 101, 31))
        self.LabelTitolo.setStyleSheet("color: white; font-family: Verdana; font-size: 24px;")
        self.LabelTitolo.setObjectName("LabelTitolo")

        #Pulsante Visualizza Ordine
        self.ButtonVisualizzaOrdine = QtWidgets.QPushButton(self.CentralWidget)
        self.ButtonVisualizzaOrdine.setGeometry(QtCore.QRect(770, 170, 231, 81))
        self.ButtonVisualizzaOrdine.setStyleSheet(self.stileButton())
        self.ButtonVisualizzaOrdine.setObjectName("ButtonVisualizzaOrdine")
        self.ButtonVisualizzaOrdine.setFocusPolicy(QtCore.Qt.NoFocus)

        #Lista Ordini
        self.ListaOrdini = QtWidgets.QListWidget(self.CentralWidget)
        self.ListaOrdini.setGeometry(QtCore.QRect(30, 180, 721, 441))
        self.ListaOrdini.setObjectName("ListaOrdini")

        altezzaBarraAlta = 51  # Altezza della barra
        altezzaData = 30  # Altezza del widget data
        centroVerticale = (altezzaBarraAlta - altezzaData) // 2

        #Data
        self.LabelData = QtWidgets.QDateEdit(self.CentralWidget)
        self.LabelData.setGeometry(QtCore.QRect(10, centroVerticale, 100, altezzaData))
        self.LabelData.setStyleSheet(self.stileData())
        self.LabelData.setDate(QtCore.QDate.currentDate())
        self.LabelData.setDisplayFormat("dd/MM/yyyy")
        self.LabelData.setCalendarPopup(True)
        self.LabelData.setObjectName("LabelDataTime")

        #Filtro per tipo
        self.LabelTitoloFiltro = QtWidgets.QLabel(self.CentralWidget)
        self.LabelTitoloFiltro.setGeometry(QtCore.QRect(30, 70, 141, 31))
        self.LabelTitoloFiltro.setStyleSheet("font-family: Verdana; font-size: 18px; color: #1E2230; font-weight: bold;")
        self.LabelTitoloFiltro.setObjectName("LabelTitoloFiltro")

        self.comboBoxFiltroTipoOrdine = QtWidgets.QComboBox(self.CentralWidget)
        self.comboBoxFiltroTipoOrdine.setGeometry(QtCore.QRect(30, 110, 721, 31))
        self.comboBoxFiltroTipoOrdine.setStyleSheet(self.stileComboBox())
        self.comboBoxFiltroTipoOrdine.setObjectName("comboBoxFiltroTipoOrdine")

        #Icone nella barra superiore
        larghezzaIcona = 25  #Dimensioni delle icone
        sapziatura = 10
        inizioX = 980
        altezzaBarraAlta = 51  #Altezza della barra
        centroVerticale = (altezzaBarraAlta - larghezzaIcona) // 2  #Calcola il centro verticale

        self.ButtonTendina = SvgIcon(":/immaginifinestrahome/9042808_menu_icon.svg", self.CentralWidget)
        self.ButtonTendina.setGeometry(
            QtCore.QRect(inizioX, centroVerticale, larghezzaIcona, larghezzaIcona))  #Usa il centro verticale
        self.ButtonTendina.setObjectName("ButtonTendina")

        self.ButtonUtenteConnesso = SvgIcon(":/immaginifinestrahome/9042880_profile_circled_icon.svg",
                                            self.CentralWidget)
        self.ButtonUtenteConnesso.setGeometry(
            QtCore.QRect(inizioX - larghezzaIcona - sapziatura, centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonUtenteConnesso.setObjectName("ButtonUtenteConnesso")

        self.ButtonInfoSoftware = SvgIcon(":/immaginifinestrahome/9042463_language_icon.svg", self.CentralWidget)
        self.ButtonInfoSoftware.setGeometry(
            QtCore.QRect(inizioX - 2 * (larghezzaIcona + sapziatura), centroVerticale, larghezzaIcona, larghezzaIcona))
        self.ButtonInfoSoftware.setObjectName("ButtonInfoSoftware")

        FinestraListaOrdini.setCentralWidget(self.CentralWidget)
        self.aggiornaTestiInterfaccia(FinestraListaOrdini)
        QtCore.QMetaObject.connectSlotsByName(FinestraListaOrdini)

    def aggiornaTestiInterfaccia(self, FinestraListaOrdini):
        trad = QtCore.QCoreApplication.translate
        FinestraListaOrdini.setWindowTitle(trad("FinestraListaOrdini", "Lista Ordini"))
        self.LabelTitolo.setText(trad("FinestraListaOrdini", "Ordini"))
        self.LabelTitoloFiltro.setText(trad("FinestraListaOrdini", "Filtro per tipo:"))
        self.ButtonVisualizzaOrdine.setText(trad("FinestraListaOrdini", "Visualizza Ordine"))

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

    def stileComboBox(self):
        return """
        QComboBox {
            font-family: "Verdana";
            font-size: 14px;
            color: #D3D3D3; /* Testo grigio chiaro */
            background-color: #283747; /* Sfondo blu scuro */
            border: 1px solid #FFFFFF; /* Bordo bianco */
            border-radius: 4px;
            padding: 5px;
        }
        QComboBox QAbstractItemView {
            background-color: #283747; /* Sfondo blu scuro per il menu a discesa */
            selection-background-color: #1E2230; /* Sfondo più scuro per l'elemento selezionato */
            selection-color: #FFFFFF; /* Testo bianco per l'elemento selezionato */
            color: #D3D3D3; /* Testo grigio chiaro */
        }
        """


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FinestraListaOrdini = QtWidgets.QMainWindow()
    ui = Ui_FinestraListaOrdini()
    ui.configurazioneInterfaccia(FinestraListaOrdini)
    FinestraListaOrdini.show()
    sys.exit(app.exec_())
