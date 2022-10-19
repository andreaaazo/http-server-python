def register(utente, password):
    engine = open("lib/components/database.txt", "a")
    engine.write(f"{utente},{password}|")
    engine.close()


def check_if_user_exists(utente_dato, password_data):
    engine = open("lib/components/database.txt", "r")
    database = engine.read()
    utenti = database.split("|")

    for utente in utenti:
        utente_presente = utente.split(",")[0]
        password_presente = utente.split(",")[1]
        if utente_presente == utente_dato and password_presente == password_data:
            return True
    return False
