# Progetto Reti di Calcolatori

Ancora difficile da dire se sarà possibile o meno, ma in caso l'idea è nel main stesso

    PROGETTO
    Costruire un socket sicuro di connessione che supporti

     - Confidentiality
     - Integrity
     - Authentication

    es. Server in ascolto, alla connessione scambia PSK e la usa per autenticare client. Una volta fatto
        invia al client una chiave simmetrica di sessione, criptata con chiave pubblica del client.

        Una volta connesso per invio e ricezione dei pacchetti utilizza una funzione send() sicura, che utilizzi
        autenticazione criptata, con verifica della firma digitale
