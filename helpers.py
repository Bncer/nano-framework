from transliterate import translit


def send_response(resp, conn, match):
    if match:
        conn.sendall(resp.encode())
        conn.close()



orig = input("")

tr = translit(orig, "ru", reversed=True)
