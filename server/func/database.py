def register(utente, password):
    engine = open("database/database.txt", "a")
    engine.write(f"{utente},{password}|")
    engine.close()


def check_if_user_exists(utente_dato, password_data):
    engine = open("database/database.txt", "r")
    database = engine.read()
    engine.close()
    utenti = database.split("|")

    for utente in utenti:
        credenziali = utente.split(",")
        if credenziali[0] == utente_dato and credenziali[1] == password_data:
            return True
    return False


def add_test_result(mark: int, user: str, test_number: int):
    engine = open(f"database/{test_number}_test_results.txt", "r")
    database = engine.read()
    engine.close()
    utenti = database.split("|")
    del utenti[-1]

    utenti_aggiornata = ""
    found = False

    for utente in utenti:
        credenziali = utente.split(",")
        if credenziali[0] == user:
            utenti_aggiornata = str(utenti_aggiornata) + f"{credenziali[0]},{mark}|"
            found = True
        else:
            utenti_aggiornata = (
                str(utenti_aggiornata) + f"{credenziali[0]}, {credenziali[1]}|"
            )

    if not found:
        utenti_aggiornata = str(utenti_aggiornata) + f"{user},{mark}|"

    engine = open(f"database/{test_number}_test_results.txt", "w")
    engine.write(str(utenti_aggiornata))
    engine.close()


def retrieve_marks_from_tests(user: str):
    engine1 = open("database/1_test_results.txt", "r")
    engine2 = open("database/2_test_results.txt", "r")
    engine3 = open("database/3_test_results.txt", "r")

    database1 = engine1.read()
    database2 = engine2.read()
    database3 = engine3.read()

    engine1.close()
    engine2.close()
    engine3.close()

    test1_marks = database1.split("|")
    test2_marks = database2.split("|")
    test3_marks = database3.split("|")

    mark1 = 0
    mark2 = 0
    mark3 = 0

    for test in test1_marks:
        credentials = test.split(",")
        if credentials[0] == user:
            mark1 = credentials[1]

    for test in test2_marks:
        credentials = test.split(",")
        if credentials[0] == user:
            mark2 = credentials[1]

    for test in test3_marks:
        credentials = test.split(",")
        if credentials[0] == user:
            mark3 = credentials[1]

    return mark1, mark2, mark3
