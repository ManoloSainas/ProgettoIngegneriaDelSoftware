# ProgettoFinaleISW
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

Ingegneria del
Software - PROGETTO

Si richiede:
● La formulazione dei requisiti usando User Stories o Casi d'Uso, con relativo diagramma
UML. In tale formulazione, a partire dalle specifiche riportate in questo documento, il
gruppo ha libertà di interpretazione in caso di dubbi o ambiguità

● La produzione di un diagramma delle classi, 2 diagrammi di sequenza ed eventuali altri
diagrammi UML (max. 2) se ritenuti utili

● Modellare e sviluppare il sistema proposto in linguaggio Python usando il
framework Django, producendo del codice comprensibile (intention revealing
code).

● Realizzare un numero sufficiente di test unitari (UT).

● Realizzare un numero sufficiente di test di accettazione (AT).

Sviluppare un'applicazione web per la gestione di un negozio di(di un negozio fisico).
L'applicazione deve permettere agli utenti di registrarsi come clienti e di effettuare l'accesso al
sistema.
Una volta loggati, i clienti possono navigare attraverso i prodotti disponibili nel negozio, visualizzare i
dettagli di ciascun prodotto e aggiungerli al carrello.
https://localhost/home
FIltri Logout
Nome
Prodotto
tipologia descrizione prezzo quantita Azione
iphone 14 cellulare smartphone di ultima
generazione
30$ 1 aggiungi al
carrello
. . . . . . . . . . . . . . .
Dalla pagina del carrello, i clienti possono visualizzare tutti i prodotti che hanno
selezionato, modificarne la quantità o rimuoverli completamente.
https://localhost/carrello
Home Logout
Nome
Prodotto
tipologia quantità Azione Prezzo
iphone 14 cellulare 1 rimuovi 30$
. . . . . . . . . . . . . . .
Totale 400$
Checkout
Al momento del checkout, i clienti devono inserire le informazioni di spedizione e di
pagamento per completare l'acquisto.
https://localhost/checkout
Carrello
Indirizzo:
Metodo Di pagamento :
Ordina
Gli amministratori del sistema possono accedere tramite un account amministratore e
hanno la possibilità di gestire i prodotti disponibili nel negozio. Possono aggiungere nuovi
prodotti, modificare i dettagli dei prodotti esistenti e rimuovere i prodotti dal negozio.
https://localhost/Home_amministratore
FIltri Aggiungi Prodotto Logout
Nome
Prodotto
tipologia descrizione prezzo Disponibilità Azione
iphone 14 cellulare smartphone di ultima
generazione
30$ 100 Modifica
. . . . . . . . . . . . . . .
Resoconto vendite
Inoltre, gli amministratori possono visualizzare un resoconto delle vendite, inclusi i
dettagli degli ordini effettuati dai clienti, l'importo totale delle vendite e altre statistiche
pertinenti.
https://localhost/Resoconto_vendite
Home FIltri
Nome
Prodotto
tipologia prezzo N° pezzi venduti Totale
iphone 14 cellulare 30$ 100 3000$
. . . . . . . . . . . . . . .
Filtri Totale vendite 10000 $
L'applicazione dovrebbe anche includere un sistema di ricerca per consentire ai clienti di
cercare prodotti specifici utilizzando parole chiave o filtri come categoria, prezzo, ecc.
