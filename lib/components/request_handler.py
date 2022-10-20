from http.server import BaseHTTPRequestHandler

from settings import *

from lib.func.template_engine import render_template, render_dashboard
from lib.func.retrieve_form_data import retrieve_fields
from lib.func.database import register, check_if_user_exists
from lib.func.cookies import (
    check_if_user_is_already_logged,
    render_dashboard_with_user_cookies,
)
from lib.func.requests import (
    send_response_302,
    send_response_200,
    send_response_302_with_user_cookie,
)


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        status = self.page_requested_status()
        if status == 404:
            self.send_response(404)
        elif status == 200:
            self.send_requested_page()

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
            send_response_302_with_user_cookie(self, "/dashboard", utente)

        nuovo_utente, password = get_fields()
        register(nuovo_utente, password)
        redirect(nuovo_utente)

    def authentication(self):
        def fields():
            d_fields = retrieve_fields(self, ["utente", "password"])
            return d_fields["utente"], d_fields["password"]

        def redirect(check, utente):
            if not check:
                page = render_template(URLPATTERNS["/credenziali_errate"])
                send_response_200(self, page)
            else:
                send_response_302_with_user_cookie(self, "/dashboard", utente)

        utente_dato, password_data = fields()
        check = check_if_user_exists(utente_dato, password_data)
        redirect(check, utente_dato)

    def send_requested_page(self):
        if self.path == "/dashboard":
            check = check_if_user_is_already_logged(self)

            if check:
                template_page = render_dashboard_with_user_cookies(self)
                send_response_200(self, template_page)
            else:
                send_response_302(self, "/errore")

        elif self.path == "/accesso" or self.path == "/registrazione":
            check = check_if_user_is_already_logged(self)

            if check:
                send_response_302(self, "/dashboard")
            else:
                rendered_page = render_template(URLPATTERNS[self.path])
                send_response_200(self, rendered_page)

        else:
            template_page = render_template(URLPATTERNS[self.path])
            send_response_200(self, template_page)
