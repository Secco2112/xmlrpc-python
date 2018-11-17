import xmlrpc.client

class RPCClient:
    def __init__(self):
        self._server_config = None
        self._client = xmlrpc.client
        self._proxy = None

    def connect(self, host="localhost", port=12345):
        self._server_config = (host, port)
        self._proxy = self._client.ServerProxy("http://"+self._server_config[0]+":"+str(self._server_config[1]))
        print("Cliente conectado na porta %s..." %(port))

    def execute(self, function_name, *args):
        method = getattr(self._proxy, function_name)
        print("Função \"%s\" chamada..." %(function_name))
        return method(*args)
