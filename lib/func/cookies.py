import cgi
from this import d
from lib.func.database import retrieve_marks_from_tests
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

    return render_dashboard(str(cookie), str(mark1), str(mark2), str(mark3))


def retrieve_current_user(handler: object):
    cookie, rest = cgi.parse_header(handler.headers.get("Cookie"))
    return cookie
