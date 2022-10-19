import cgi
from settings import *
from .template_engine import *


def check_for_cookies_render_dashboard(self, ifFalse_redirect_path):
    try:
        cookie, rest = cgi.parse_header(self.headers.get("Cookie"))
        return render_dashboard(str(cookie))
    except TypeError:
        return render_template(URLPATTERNS[ifFalse_redirect_path])
