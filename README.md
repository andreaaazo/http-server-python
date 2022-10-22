<h1 align="center">Compito di informatica</h1>
<p align="center">Andrea Zorzi 4M</p>

## Introduzione
Buongiorno professore,
in questo file può trovare il mio compito di informatica. Mi sono permesso di espandere il progetto, introducendo un gestore di richieste, ed un server HTTP base.  

<br>

Inizialmente il sito web si presenta con una pagina introduttiva, dove potrà scegliere di registrarsi oppure di accedere ad un profilo già registrato.  
Una volta eseguito correttamente l'accesso, il server la reinderizzerà in una pagina utente, dove verranno mostrati i 3 test che potrà eseguire. In basso può trovare il voto assegnato al test e il numero di domande a cui ha risposto in modo corretto.

<br>

Il server funziona tramite dei cookies, che permettono di mantenere la sessione attiva. Per cui anche se aprirà una nuova finestra sul browser e vorrà accedere al proprio account, il server farà l'accesso in maniera automatica, senza dover reinserire le credenziali in maniera totalmente reattiva.

<br>

Per facilitare la buona esecuzione del codice mi sono permesso di aggiungere un ambiente python virtuale. 

<br>

Il mio codice è online al seguente link: [GitHub](https://github.com/andreaaazo/http-server-python) ed a breve posterò un timelapse della creazione del codice su [YouTube](https://www.youtube.com/channel/UCAMPX_yvXMXMidga9hTYyAQ).

## Struttura del codice
Il codice si presenta in questo modo:
```
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── database
│   ├── 1_correct_answers.txt
│   ├── 1_test_results.txt
│   ├── 2_correct_answers.txt
│   ├── 2_test_results.txt
│   ├── 3_correct_answers.txt
│   ├── 3_test_results.txt
│   └── database.txt
├── main.py
├── server
│   ├── func
│   │   ├── __init__.py
│   │   ├── cookies.py
│   │   ├── database.py
│   │   ├── requests.py
│   │   ├── retrieve_form_data.py
│   │   ├── template_engine.py
│   │   └── test_check.py
│   ├── http_request_handler.py
│   └── http_server.py
├── settings.py
└── templates
    ├── accesso.html
    ├── credenziali_errate.html
    ├── dashboard.html
    ├── errore.html
    ├── home.html
    ├── registrazione.html
    ├── test1.html
    ├── test2.html
    └── test3.html

4 directories, 31 files
```

I 2 file più importanti sono: `main.py` e `settings.py`.  

All'interno del file `settings.py`, può trovare alcune impostazioni (create da me) per facilitare la gestione del server.  
Invece `main.py` è il codice principale per far eseguire il server.

<br>

La cartella `templates` contiene i file HTML utilizzati dal server.  

<br>

La cartella `server` contiene i componenti principali riguardanti il server: un gestore di richieste ed il server vero e proprio.  
Mentre nella sottocartella `func` può trovare tutte le funzioni utilizate dal server e dal gestore.  

<br>

La cartella `database`contiene tutte le "tabelle" o file .txt per il salvataggio permanente dei dati.

<br>

Gli altri files sono soltanto per i comandi `git` e `pip` e ho allegato un file .txt contenente una licenza MIT (per GitHub).



## Come eseguire il codice
1. Aprire il terminale
2. **Andare** con il terminale **nella cartella principale**: `cd http-server-python`
3. **Attivare l'ambiente virtuale python** creato da me: `pipenv shell`
4. **Digitare nel terminale**: `python main.py`
5. Con un browser a sua scelta **andare al seguente link**: `http://localhost:8000`

