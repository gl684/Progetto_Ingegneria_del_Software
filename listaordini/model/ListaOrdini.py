import json
import os
import pickle

from ordine.model.Ordine import Ordine, Fase


class ListaOrdini:
    def __init__(self):
        self.lista_ordini = []
        self.carica_dati()

    def carica_dati(self):

        file_pickle = 'C:/Users/glgia/OneDrive/Documents/tirocinio/implementazione progetto/listaordini/data/lista_ordini_salvata.pickle'
        file_json = 'C:/Users/glgia/OneDrive/Documents/tirocinio/implementazione progetto/listaordini/data/lista_ordini_iniziali.json'

        #Stampa i percorsi dei file
        print(f"Percorso pickle: {os.path.abspath(file_pickle)}")
        print(f"Percorso JSON: {os.path.abspath(file_json)}")

        #Verifica l'esistenza dei file
        print(f"Il file pickle esiste? {os.path.exists(file_pickle)}")
        print(f"Il file JSON esiste? {os.path.exists(file_json)}")

        try:
            if os.path.exists(file_pickle):
                with open(file_pickle, 'rb') as f:
                    self.lista_ordini = pickle.load(f)
                print("Dati caricati dal file pickle")
            elif os.path.exists(file_json):
                with open(file_json, 'r') as f:
                    data = json.load(f)
                    self.lista_ordini = [
                        Ordine(
                            nome_ordine=ordine['nome_ordine'],
                            oggetto_ordine=ordine['oggetto_ordine'],
                            data_inizio=ordine["data_inizio"],
                            data_termine=ordine["data_termine"],
                            stato=ordine["stato"],
                            numero_fasi=ordine["numero_fasi"],
                            list_fasi=[
                                Fase(
                                    numero_fase=fase['numero_fase'],
                                    nome_fase=fase['nome_fase'],
                                    esternalizzazione_fase=fase["esternalizzata"],
                                    stato_fase=fase['stato_fase']
                                ) for fase in ordine['fasi']
                            ],
                            id_ordine=ordine.get("id_ordine")  # Assicura il recupero dell'id_ordine, se esistente
                        )
                        for ordine in data
                    ]
                print("Dati caricati dal file JSON")
            else:
                print(f"Entrambi i file non esistono: {file_pickle}, {file_json}")
        except Exception as e:
            print(f"Errore nel caricamento dei dati: {e}")


    def salva_dati(self):
        """Salva i dati degli ordini in un file pickle."""
        with open('listaordini/data/lista_ordini_salvata.pickle', 'wb') as f:
            pickle.dump(self.lista_ordini, f, pickle.HIGHEST_PROTOCOL)

    def get_ordine_da_indice(self, index):
        """Restituisce un ordine dato l'indice."""
        return self.lista_ordini[index]

    def get_lista_ordini(self):
        return self.lista_ordini

    def get_lista_ordini_filtrata(self, tipo_ordine):
        """Restituisce una lista filtrata per tipo di ordine."""
        return [ordine for ordine in self.lista_ordini if ordine.oggetto_ordine == tipo_ordine]
