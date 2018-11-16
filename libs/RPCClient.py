import xmlrpc.client


class RPCClient:
    def __init__(self):
        self.server_config = None
        self.client = xmlrpc.client
        self.proxy = None

    def connect(self, host="localhost", port=12345):
        self.server_config = (host, port)
        self.proxy = self.client.ServerProxy("http://"+self.server_config[0]+":"+str(self.server_config[1]))
        print("Cliente conectado na porta %s..." %port)

    def execute(self, function_name, *args):
        method = getattr(self.proxy, function_name)
        return method(*args)
