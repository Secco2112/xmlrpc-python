from libs.RPCServer import RPCServer
from libs.RPCFunctions import RPCFunctions

rpc_functions = RPCFunctions()
functions = {
    "add": rpc_functions.add,
    "is_even": rpc_functions.is_even,
    "is_prime": rpc_functions.is_prime,
    "is_even_xml": rpc_functions.is_even_xml,
}

server = RPCServer()
server.connect()
server.register_functions(functions)
server.start()
