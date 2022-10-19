def render_template(path):
    engine = open(f"templates/{path}")
    template = engine.read()
    engine.close()
    return template


def render_dashboard(nome_utente):
    engine = open(f"templates/dashboard.html")
    file_page = engine.read()
    template = file_page.format(nome_utente=str(nome_utente))
    engine.close()
    return template
