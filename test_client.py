from libs.RPCClient import RPCClient

client = RPCClient()
client.connect()

function_call = client.execute("is_even", 9)
print(function_call)
