from server.http_server import Server
from settings import HOSTNAME, PORT

if __name__ == "__main__":
    server = Server()
    print(
        f"""
    Server started at http://{HOSTNAME}:{PORT}
    -----
    Press CRTL-C to stop
    """
    )

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped")
