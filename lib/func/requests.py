def send_response_302(handler: object, location: str):
    handler.send_response(302)
    handler.send_header("Location", location)
    # handler.send_header("Content-type", "text/html")
    handler.end_headers()
    # handler.wfile.write(bytes(str(rendered_template), "utf-8"))


def send_response_302_with_user_cookie(
    handler: object, location: str, cookie_name: str
):
    handler.send_response(302)
    handler.send_header("Set-Cookie", cookie_name)
    handler.send_header("Location", location)
    # handler.send_header("Content-type", "text/html")
    handler.end_headers()
    # handler.wfile.write(bytes(str(rendered_template), "utf-8"))


def send_response_200(handler: object, rendered_page: str):
    handler.send_response(200)
    handler.send_header("Content-type", "text/html")
    handler.end_headers()
    handler.wfile.write(bytes(str(rendered_page), "utf-8"))
