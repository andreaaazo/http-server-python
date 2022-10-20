def register(utente, password):
    engine = open("lib/components/database.txt", "a")
    engine.write(f"{utente},{password}|")
    engine.close()


def check_if_user_exists(utente_dato, password_data):
    engine = open("lib/components/database.txt", "r")
    database = engine.read()
    utenti = database.split("|")

    for utente in utenti:
        credenziali = utente.split(",")
        if credenziali[0] == utente_dato and credenziali[1] == password_data:
            return True
    return False
