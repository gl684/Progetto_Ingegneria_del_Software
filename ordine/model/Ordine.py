from typing import List
import uuid

class Fase:
    def __init__(self,
                 numero_fase: int,
                 nome_fase: str,
                 esternalizzazione_fase: bool,
                 stato_fase: str):
        self.numero_fase = numero_fase
        self.nome_fase = nome_fase
        self.dettagli_fase = None  # inizializzazione a None
        self.esternalizzazione_fase = esternalizzazione_fase
        self.stato_fase = stato_fase
        self.resoconto_fase = None  # inizializzazione a None
        self.durata_fase = None  # inizializzazione a None

class Ordine:
    def __init__(self,
                 nome_ordine: str,
                 oggetto_ordine: str,
                 data_inizio: str,
                 data_termine: str,
                 stato: str,
                 numero_fasi: int,
                 list_fasi: List[Fase],
                 id_ordine: str = None):
        self.id_ordine = id_ordine or str(uuid.uuid4())  # Genera un ID univoco se non fornito
        self.nome_ordine = nome_ordine
        self.oggetto_ordine = oggetto_ordine
        self.data_inizio = data_inizio
        self.data_termine = data_termine
        self.stato = stato
        self.numero_fasi = numero_fasi
        self.list_fasi = list_fasi
