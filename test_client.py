from libs.RPCClient import RPCClient

for i in range(1, 1000):
    client = RPCClient()
    client.connect()

    function_call = client.execute("is_even", 9)
    print(function_call)
