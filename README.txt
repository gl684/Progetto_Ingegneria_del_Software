Progetto per tirocinio in Ingegneria del Software A.A. 2024/2025

Questo progetto consiste nella realizzazione di un software gestionale per una tipografia.
Le funzionalità implementate sono:
1) CRUD Cliente
2) Filtro Ordini
1) Visualizzazione Ordine

L'implementazione del progetto inizia dalla Home, anche se nella documentazione della progettazione del software è prevista
l'implementazione di un login iniziale che riconosce le credenziali dell'utente e deinisce il suo livello di accesso alle
varie funzionalita delle aree di gestione del programma.

1) La funzionalità CRUD cliente è stata pensata in questo modo: dalla lista degli cliente è possibile selezionare un cliente
e aprirlo per visualizzarlo nel dettaglio, se non si seleziona alcun cliente quando si preme il bottone Apri apparirà un messaggio
di errore. Una volta visualizzato il dettaglio del cliente, l'utente può scegliere di modiicarlo, eliminarlo o chiudere
la finestra per tornare alla finestra precedente.

2)Il Filtro Ordini è un filtro dinamico che genera le sue opzioni in base ai tipi degli ordini presenti nel file e consente
appunto di filtrare gli ordini per tipo.

3) La visualizzazione di un ordine consente di visualizzare i dettagli di un ordine sia nelle sue caratteristiche geerali
che nella sua struttura interna attraverso una tabella che indica anche alcuni dettagli relativi alle singole fasi.
Nella documentazione del progetto sono previste anche funzionalità che consentono ai singoli operatori di accedere al software,
una volta completata la propria fase di lavoro e aggiungere dettagli sullo svolgimento della fase stessa, utili alla corretta
gestione della tipografia e ad una rapida revisione dello svolgimento delle attività da parte della direzione.

E' stato utilizzato il linguaggio Python con la libreria PyQt5 per l'interfaccia grafica.
La documentazione del progetto è tra i file della repository sotto la  voce Documentazione_progetto_software_tipografia.pdf
