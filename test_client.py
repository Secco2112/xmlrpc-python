from libs.RPCClient import RPCClient

client = RPCClient()
client.connect()

function_call = client.execute("is_even_xml", 10)
print(function_call)
