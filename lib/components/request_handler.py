from http.server import BaseHTTPRequestHandler
from settings import *
from lib.functions.template_engine import render_dashboard, render_template
from lib.functions.retrieve_form_data import retrieve_fields
import cgi


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status = self.page_requested_status()
        if status == 404:
            self.send_response(404)
        elif status == 200:
            self.render_template()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(str(self.render_template()), "utf-8"))

    def do_POST(self):
        if self.path == "/accesso":
            self.authentication()
        elif self.path == "/registrazione":
            self.register()

    def page_requested_status(self):
        if self.path in URLPATTERNS:
            return 200
        else:
            return 404

    def register(self):
        def fields():
            d_fields = retrieve_fields(self, ["nuovo_utente", "password"])
            return d_fields["nuovo_utente"], d_fields["password"]

        def register(utente, password):
            engine = open("lib/components/database.txt", "a")
            engine.write(f"{utente},{password}|")
            engine.close()

        def redirect(utente):
            self.send_response(302)
            self.send_header("Set-Cookie", f"{utente}")
            self.send_header("Location", "/dashboard")
            self.end_headers()

        nuovo_utente, password = fields()
        register(nuovo_utente, password)
        redirect(nuovo_utente)

    def authentication(self):
        def fields():
            d_fields = retrieve_fields(self, ["utente", "password"])
            return d_fields["utente"], d_fields["password"]

        def check_if_user_is_registered(utente_dato, password_data):
            engine = open("lib/components/database.txt", "r")
            database = engine.read()
            utenti = database.split("|")

            for utente in utenti:
                if (
                    utente.split(",")[0] == utente_dato
                    and utente.split(",")[1] == password_data
                ):
                    return True

        def redirect(check):
            self.send_response(302)
            if not check:
                self.send_header("Location", "/credenziali_errate")
            else:
                self.send_header("Location", "/dashboard")
            self.end_headers()

        utente_dato, password_data = fields()
        check = check_if_user_is_registered(utente_dato, password_data)
        redirect(check)

    def render_template(self):
        if self.path == "/dashboard":
            try:
                cookie, rest = cgi.parse_header(self.headers.get("Cookie"))
                return render_dashboard(str(cookie))
            except TypeError:
                return render_template(URLPATTERNS["/errore"])

        elif self.path == "/accesso" or self.path == "/registrazione":
            try:
                cookie, rest = cgi.parse_header(self.headers.get("Cookie"))
                return render_dashboard(str(cookie))
            except TypeError:
                return render_template(URLPATTERNS[self.path])
        else:
            return render_template(URLPATTERNS[self.path])
