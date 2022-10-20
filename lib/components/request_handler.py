from http.server import BaseHTTPRequestHandler

from settings import *

from lib.func.template_engine import render_template, render_dashboard
from lib.func.retrieve_form_data import retrieve_fields
from lib.func.database import register, check_if_user_exists, add_test_result
from lib.func.cookies import (
    check_if_user_is_already_logged,
    render_dashboard_with_user_cookies,
    retrieve_current_user,
)
from lib.func.requests import (
    send_response_302,
    send_response_200,
    send_response_302_with_user_cookie,
)
from lib.func.test_check import correct_results, calculate_mark


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
        elif self.path == "/test1":
            self.update_results(
                [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                ],
                {
                    "1": "2",
                    "2": "2",
                    "3": "1",
                    "4": "0",
                    "5": "0",
                    "6": "0",
                    "7": "0",
                    "8": "2",
                },
                8,
                1,
            )
        elif self.path == "/test2":
            self.update_results(
                [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                ],
                {
                    "1": "2",
                    "2": "2",
                    "3": "1",
                    "4": "0",
                    "5": "0",
                    "6": "0",
                    "7": "0",
                    "8": "2",
                },
                8,
                2,
            )
        elif self.path == "/test3":
            self.update_results(
                [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                ],
                {
                    "1": "2",
                    "2": "2",
                    "3": "1",
                    "4": "0",
                    "5": "0",
                    "6": "0",
                    "7": "0",
                    "8": "2",
                },
                8,
                3,
            )
        elif self.path == "/dashboard":
            send_response_302_with_user_cookie(
                self,
                "/",
                "=deleted; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT",
            )

    def page_requested_status(self):
        if self.path in URLPATTERNS:
            return 200
        else:
            return 404

    def update_results(
        self,
        values_list: list,
        answers: list,
        number_of_questions: int,
        test_number: int,
    ):
        correct_responses_number = correct_results(
            self,
            values_list,
            answers,
        )
        mark = calculate_mark(correct_responses_number, number_of_questions)
        current_user = retrieve_current_user(self)
        add_test_result(mark, current_user, test_number)
        send_response_302(self, "/dashboard")

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
