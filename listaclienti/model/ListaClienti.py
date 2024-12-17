import pickle
import os

class ListaClienti:
    def __init__(self):
        self.lista_clienti = []
        self.carica_dati()  #Carica i dati salvati all'avvio

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)
        self.salva_dati()  #Salva i dati dopo l'aggiunta di un cliente

    def get_lista_clienti(self):
        return self.lista_clienti

    def get_cliente_da_indice(self, index):
        if 0 <= index < len(self.lista_clienti):
            return self.lista_clienti[index]
        return None

    def rimuovi_cliente_da_id(self, cliente_id):
        self.elimina_cliente(cliente_id)

    def elimina_cliente(self, cliente_id):
        self.lista_clienti = [cliente for cliente in self.lista_clienti if cliente.id != cliente_id]
        self.salva_dati()  #Salva i dati dopo l'eliminazione di un cliente

    def modifica_cliente(self, cliente_modificato):
        for i, cliente in enumerate(self.lista_clienti):
            if cliente.id == cliente_modificato.id:
                self.lista_clienti[i] = cliente_modificato  # Aggiorna il cliente
                break
        self.salva_dati()  #Salva i dati dopo la modifica

    def salva_dati(self):
        try:
            #Assicurati che la directory esista
            directory = 'listaclienti/data/'
            if not os.path.exists(directory):
                os.makedirs(directory)

            #Salva i dati su file pickle
            with open(f'{directory}lista_clienti_salvata.pickle', 'wb') as handle:
                pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)
                print(f"Clienti salvati correttamente: {self.lista_clienti}")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")

    def carica_dati(self):
        try:
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as handle:
                self.lista_clienti = pickle.load(handle)
                print(f"Clienti caricati correttamente: {self.lista_clienti}")
        except FileNotFoundError:
            print("File dei clienti non trovato, inizializzazione con lista vuota.")
            self.lista_clienti = []
        except Exception as e:
            print(f"Errore durante il caricamento: {e}")
            self.lista_clienti = []

