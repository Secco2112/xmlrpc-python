from libs.RPCClient import RPCClient

client = RPCClient()
client.connect()

function_call = client.execute("is_even", 569)
print(function_call)

