import stanza
import jsonrpc
from simplejson import loads

# stanza.download('en')
# nlp = stanza.Pipeline('en')
# doc = nlp("Barack Obama was born in Hawaii.")
# print(doc)
# print(doc.entities)

# stanza.install_corenlp()
# TOO COMPLICATED
# stanza.download_corenlp_models(model='english-kbp', version='4.2.2')
# server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
#                              jsonrpc.TransportTcpIp(addr=("127.0.0.1", 8080)))
#
# result = loads(server.parse("Hello world.  It is so beautiful"))
# print ("Result" + result)