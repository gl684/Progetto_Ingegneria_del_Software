import uuid

class Cliente:
    def __init__(self, email, telefono, indirizzo, tipo_cliente, id=None, nome=None, cognome=None, cf=None, nome_azienda=None, partita_iva=None):
        self.id = id if id else str(uuid.uuid4())  # Genera un UUID se l'ID non è fornito
        self.email = email
        self.telefono = telefono
        self.indirizzo = indirizzo  # Campo comune spostato sopra
        self.tipo_cliente = tipo_cliente  # "Privato" o "Azienda"

        # Attributi per cliente privato
        self.nome = nome
        self.cognome = cognome
        self.cf = cf

        # Attributi per cliente azienda
        self.nome_azienda = nome_azienda
        self.partita_iva = partita_iva

    def descrizione(self):
        if self.tipo_cliente == "Privato":
            return f"Cliente Privato: {self.nome} {self.cognome}, CF: {self.cf}, Indirizzo: {self.indirizzo}, Email: {self.email}, Telefono: {self.telefono}"
        elif self.tipo_cliente == "Azienda":
            return f"Cliente Azienda: {self.nome_azienda}, P.IVA: {self.partita_iva}, Indirizzo: {self.indirizzo}, Email: {self.email}, Telefono: {self.telefono}"
        else:
            return "Tipo di cliente sconosciuto."

    def is_privato(self):
        return self.tipo_cliente == "Privato"

    def is_azienda(self):
        return self.tipo_cliente == "Azienda"
