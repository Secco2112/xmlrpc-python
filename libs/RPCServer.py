from xmlrpc.server import SimpleXMLRPCServer

class RPCServer:
    def __init__(self):
        self.server_config = None
        self.server = None
        self.functions_list = {}

    def connect(self, host="localhost", port=12345):
        self.server_config = (host, port)
        self.server = SimpleXMLRPCServer(self.server_config)
        print("O servidor RPC está rodando na porta %s..." %self.server_config[1])
        return self

    def start(self):
        self.server.serve_forever()
        return self

    def register_functions(self, functions: list):
        if len(functions) > 0:
            for name, function in functions.items():
                self.server.register_function(function, name)
                self.functions_list[name] = function
        return self

    def call(self, o, name, params=[]):
        getattr(o, name)(params)
