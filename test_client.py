from libs.RPCClient import RPCClient
from libs.ImageWebCrawler import ImageWebCrawler

iwc = ImageWebCrawler()
iwc.setPathToDownload("C:/download_images/").setUrl("https://imgur.com/")

# for i in range(1, 1000):
#     client = RPCClient()
#     client.connect()
#
#     function_call = client.execute("is_even", 9)
#     print(function_call)
