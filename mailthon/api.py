from mailthon.attachments import HTML
from mailthon.envelope import Envelope, Stamp
from mailthon.postman import Postman
from mailthon.preprocessors import TLS, Auth


def html(subject, sender, receiver, content):
    return Envelope(
        Stamp(subject, sender, receiver),
        attachments=[
            HTML(content),
        ],
    )


def postman(server, port=587, auth=(None, None), force_tls=False):
    username, password = auth
    return Postman(
        server=server,
        port=port,
        preprocessors=[
            TLS(force=force_tls),
            Auth(username, password),
        ],
    )
