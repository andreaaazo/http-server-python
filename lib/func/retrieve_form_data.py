import cgi


def retrieve_fields(self, values_names_list):
    values = dict()
    ctype, dictionary = cgi.parse_header(self.headers.get("content-type"))
    dictionary["boundary"] = bytes(dictionary["boundary"], "utf-8")
    valori_ricevuti = cgi.parse_multipart(self.rfile, dictionary)
    for valori in values_names_list:
        try:
            values[valori] = valori_ricevuti.get(str(valori))[0]
        except TypeError:
            values[valori] = None
    return values
