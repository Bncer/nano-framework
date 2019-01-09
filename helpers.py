from transliterate import translit


def send_response(resp, conn, match, text=None):
    if match:
        conn.sendall(resp.encode())
        conn.close()
        if text:
            tr = translit(text, "ru", reversed=True)
            print(tr)


"""
def trans(send_response):
    #orig = input("Type: ")
    tr = translit(text, "ru", reversed=True)
    return tr
"""
