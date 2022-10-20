import cgi
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
    return render_dashboard(str(cookie))
