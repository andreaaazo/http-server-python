def render_template(path):
    engine = open(f"templates/{path}")
    template = engine.read()
    engine.close()
    return template


def render_dashboard(
    nome_utente,
    test_1: int,
    test_2: int,
    test_3: int,
    answer_1: int,
    answer_2: int,
    answer_3: int,
):
    engine = open(f"templates/dashboard.html")
    file_page = engine.read()
    template = file_page.format(
        nome_utente=str(nome_utente),
        test_1=str(test_1),
        test_2=str(test_2),
        test_3=str(test_3),
        answer_1=str(answer_1),
        answer_2=str(answer_2),
        answer_3=str(answer_3),
    )
    engine.close()
    return template
