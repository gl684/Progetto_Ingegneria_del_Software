from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ordine.views import img_rc


class SvgIcon(QtSvg.QSvgWidget):
    def __init__(self, svg_path, parent=None):
        super(SvgIcon, self).__init__(svg_path, parent)
        self.svg_path = svg_path


class Ui_FinestraVisualizzaOrdine(object):
    def configurazioneInterfaccia(self, FinestraVisualizzaOrdine):
        FinestraVisualizzaOrdine.setObjectName("FinestraVisualizzaOrdine")
        FinestraVisualizzaOrdine.resize(801, 691)
        FinestraVisualizzaOrdine.setFixedSize(801, 691)

        self.CentralWidget = QtWidgets.QWidget(FinestraVisualizzaOrdine)
        self.CentralWidget.setObjectName("centralwidget")

        #Sfondo con QLabel
        self.label = QtWidgets.QLabel(self.CentralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 691))
        self.label.setPixmap(
            QtGui.QPixmap(":/immaginifinestrahome/25101_XCDaZO.jpeg").scaled(
                801, 691, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation
            )
        )
        self.label.setScaledContents(False)  # Evita ulteriori ridimensionamenti dinamici
        self.label.setObjectName("label")

        #Barra in alto
        self.BarraAlta = QtWidgets.QLabel(self.CentralWidget)
        self.BarraAlta.setGeometry(QtCore.QRect(0, 0, 801, 41))
        self.BarraAlta.setStyleSheet("background-color: #283747; border-bottom: 2px solid white;")
        self.BarraAlta.setText("")
        self.BarraAlta.setObjectName("BarraAlta")

        #Data
        self.LabelData = QtWidgets.QDateEdit(self.CentralWidget)
        self.LabelData.setGeometry(QtCore.QRect(10, 5, 100, 30))  # Posizionamento corretto
        self.LabelData.setStyleSheet(self.stileData())
        self.LabelData.setDate(QtCore.QDate.currentDate())
        self.LabelData.setDisplayFormat("dd/MM/yyyy")
        self.LabelData.setCalendarPopup(True)
        self.LabelData.setObjectName("lblDataTime")

        #Label Visualizzazione Ordine
        self.labelVisualizzazioneOrdine = QtWidgets.QLabel(self.CentralWidget)
        self.labelVisualizzazioneOrdine.setGeometry(QtCore.QRect(280, 10, 271, 20))
        self.labelVisualizzazioneOrdine.setStyleSheet(
            "font-family: Verdana; font-size: 24px; color: #FFFFFF; font-weight: normal;"
        )
        self.labelVisualizzazioneOrdine.setObjectName("labelVisualizzazioneOrdine")

        #Definizione dimensioni e posizione delle icone
        larghezzaIcona = 20
        spaziatura = 8
        inizioX = 760
        altezzaBarraAlta = 41  # Altezza della barra
        centroVerticale = (altezzaBarraAlta - larghezzaIcona) // 2  # Calcola il centro verticale

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

        #Dettagli Ordine
        self.labelNomeOrdine = QtWidgets.QLabel(self.CentralWidget)
        self.labelNomeOrdine.setGeometry(QtCore.QRect(80, 70, 600, 21))
        self.labelNomeOrdine.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelNomeOrdine.setObjectName("labelNomeOrdine")

        self.labelOggettoOrdine = QtWidgets.QLabel(self.CentralWidget)
        self.labelOggettoOrdine.setGeometry(QtCore.QRect(80, 110, 600, 21))
        self.labelOggettoOrdine.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelOggettoOrdine.setObjectName("labelOggettoOrdine")

        self.labelDataInizio = QtWidgets.QLabel(self.CentralWidget)
        self.labelDataInizio.setGeometry(QtCore.QRect(80, 150, 600, 21))
        self.labelDataInizio.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelDataInizio.setObjectName("labelDataInizio")

        self.labelDataTermine = QtWidgets.QLabel(self.CentralWidget)
        self.labelDataTermine.setGeometry(QtCore.QRect(80, 190, 600, 21))
        self.labelDataTermine.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelDataTermine.setObjectName("labelDataTermine")

        self.labelStatoOrdine = QtWidgets.QLabel(self.CentralWidget)
        self.labelStatoOrdine.setGeometry(QtCore.QRect(80, 230, 600, 21))
        self.labelStatoOrdine.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelStatoOrdine.setObjectName("labelStatoOrdine")

        self.labelIDOrdine = QtWidgets.QLabel(self.CentralWidget)
        self.labelIDOrdine.setGeometry(QtCore.QRect(80, 270, 600, 21))
        self.labelIDOrdine.setStyleSheet("font: 63 9pt 'Sitka Text Semibold';")
        self.labelIDOrdine.setObjectName("labelIDOrdine")

        #Tabella delle Fasi
        self.TabellaFasiOrdine = QtWidgets.QTableWidget(self.CentralWidget)
        self.TabellaFasiOrdine.setGeometry(QtCore.QRect(50, 340, 681, 291))
        self.TabellaFasiOrdine.setObjectName("TabellaFasiOrdine")
        self.TabellaFasiOrdine.setColumnCount(0)
        self.TabellaFasiOrdine.setRowCount(0)

        FinestraVisualizzaOrdine.setCentralWidget(self.CentralWidget)

        self.aggiornaTestiInterfaccia(FinestraVisualizzaOrdine)
        QtCore.QMetaObject.connectSlotsByName(FinestraVisualizzaOrdine)


    def aggiornaTestiInterfaccia(self, FinestraVisualizzaOrdine):
        trad = QtCore.QCoreApplication.translate
        FinestraVisualizzaOrdine.setWindowTitle(trad("FinestraVisualizzaOrdine", "Visualizzazione Ordine"))
        self.LabelData.setDisplayFormat(trad("FinestraVisualizzaOrdine", "dd/MM/yyyy"))
        self.labelVisualizzazioneOrdine.setText(trad("FinestraVisualizzaOrdine", "Visualizzazione Ordine"))
        self.labelNomeOrdine.setText(trad("FinestraVisualizzaOrdine", "Nome Ordine:"))
        self.labelOggettoOrdine.setText(trad("FinestraVisualizzaOrdine", "Oggetto Ordine:"))
        self.labelDataInizio.setText(trad("FinestraVisualizzaOrdine", "Data di Inizio:"))
        self.labelDataTermine.setText(trad("FinestraVisualizzaOrdine", "Data Termine:"))
        self.labelStatoOrdine.setText(trad("FinestraVisualizzaOrdine", "Stato Ordine:"))
        self.labelIDOrdine.setText(trad("FinestraVisualizzaOrdine", "ID Ordine:"))

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
    FinestraVisualizzaOrdine = QtWidgets.QMainWindow()
    ui = Ui_FinestraVisualizzaOrdine()
    ui.configurazioneInterfaccia(FinestraVisualizzaOrdine)
    FinestraVisualizzaOrdine.show()
    sys.exit(app.exec_())
