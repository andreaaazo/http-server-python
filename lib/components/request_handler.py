from http.server import BaseHTTPRequestHandler

from settings import *

from lib.functions.template_engine import render_template, render_dashboard
from lib.functions.retrieve_form_data import retrieve_fields
from lib.functions.database import register, check_if_user_exists
from lib.functions.cookies import check_for_cookies_render_dashboard


class HTTPRequestHandler(BaseHTTPRequestHandler):
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
        def get_fields():
            d_fields = retrieve_fields(self, ["nuovo_utente", "password"])
            return d_fields["nuovo_utente"], d_fields["password"]

        def redirect(utente):
            self.send_response(302)
            self.send_header("Set-Cookie", f"{utente}")
            self.send_header("Location", "/dashboard")
            self.end_headers()

        nuovo_utente, password = get_fields()
        register(nuovo_utente, password)
        redirect(nuovo_utente)

    def authentication(self):
        def fields():
            d_fields = retrieve_fields(self, ["utente", "password"])
            return d_fields["utente"], d_fields["password"]

        def redirect(check):
            self.send_response(302)
            if not check:
                self.send_header("Location", "/credenziali_errate")
            else:
                self.send_header("Location", "/dashboard")
            self.end_headers()

        utente_dato, password_data = fields()
        check = check_if_user_exists(utente_dato, password_data)
        redirect(check)

    def render_template(self):
        if self.path == "/dashboard":
            return check_for_cookies_render_dashboard(self, "/errore")

        elif self.path == "/accesso" or self.path == "/registrazione":
            return check_for_cookies_render_dashboard(self, self.path)
        else:
            return render_template(URLPATTERNS[self.path])
