import cgi
from .database import retrieve_marks_from_tests, retrieve_correct_answers
from settings import *
from .template_engine import *


def check_if_user_is_already_logged(handler: object):
    try:
        cookie, rest = cgi.parse_header(handler.headers.get("Cookie"))
        return True
    except TypeError:
        return False


def render_dashboard_with_user_cookies(handler: object):
    cookie, rest = cgi.parse_header(handler.headers.get("Cookie"))
    mark1, mark2, mark3 = retrieve_marks_from_tests(str(cookie))
    answer1, answer2, answer3 = retrieve_correct_answers(str(cookie))

    return render_dashboard(
        str(cookie),
        int(mark1),
        int(mark2),
        int(mark3),
        int(answer1),
        int(answer2),
        int(answer3),
    )


def retrieve_current_user(handler: object):
    cookie, rest = cgi.parse_header(handler.headers.get("Cookie"))
    return cookie
