from decorators import address
from helpers import send_response
from renderer import render
from pymy import db_connect


@address('about')
def about_handler(request, conn, match=True, data={}):
    template = 'about.html'
    abc = render(template, {'this_is_variable': 'My site' })
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(abc)

    send_response(resp, conn, match)


@address('contacts')
def contact_handler(request, conn, match=True, data={}):
    template = 'contacts.html'
    content = render(template, {'marvel_var': db_connect()})
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(content)

    send_response(resp, conn, match)


@address('translit')
def translit_handler(request, conn, match=True):
    template = 'translit.html'
    abc = render(template, {'tran_var': "dsfsdf" })
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(abc)

    send_response(resp, conn, match)
