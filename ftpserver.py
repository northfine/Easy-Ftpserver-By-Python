from pyftplib.authorizers import DummyAuthorizer
from pyftplib.handles import FTPHandler
from pyftplib.servers import FTPServer

authorizer = DummuAuthorizer()

authorizer.add_user('user', 'somebody', '/tmp/', perm='elradfmv')

authorizer.add_anonymous('/opt/xxxx')

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(('0.0.0.0', 2121), handler)

server.serve_forever()