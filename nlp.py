# import stanza
# import jsonrpc
# from simplejson import loads

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

# --------------------------------------------------------------------------------

# import urllib.request
# from bs4 import BeautifulSoup
# import spacy
# import neuralcoref
#
# nlp = spacy.load('en_core_web_lg')
# neuralcoref.add_to_pipe(nlp)
#
# html = urllib.request.urlopen('https://www.law.cornell.edu/supremecourt/text/418/683').read()
# soup = BeautifulSoup(html, 'html.parser')
# text = ''.join([t for t in soup.find_all(text=True) if t.parent.name == 'p' and len(t) >= 25])
# doc = nlp(text)
# resolved_text = doc._.coref_resolved
# sentences = [sent.string.strip() for sent in nlp(resolved_text).sents]
# output = [sent for sent in sentences if 'president' in
#           (' '.join([token.lemma_.lower() for token in nlp(sent)]))]
# print('Fact count:', len(output))
# for fact in range(len(output)):
#     print(str(fact+1)+'.', output[fact])

# ------------------------------------------------------------------
from allennlp.predictors.predictor import Predictor

model_url = "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz"
predictor = Predictor.from_path(model_url)
text2 = "Joseph Robinette Biden Jr. is an American politician who is the 46th and\
current president of the United States. A member of the Democratic Party, \
he served as the 47th vice president from 2009 to 2017 under Barack Obama and\
represented Delaware in the United States Senate from 1973 to 2009."
text = "Eleni is hot. She really needs a cookie."


prediction = predictor.predict(document=text)  # get prediction
#print("Clsuters:-")
#for cluster in prediction['clusters']:
#    print(cluster)  # list of clusters (the indices of spaCy tokens)
# Result: [[[0, 3], [26, 26]], [[34, 34], [50, 50]]]
#print('\n\n') #Newline

#print('Coref resolved: ',predictor.coref_resolved(text))  # resolved text
# Result: Joseph Robinette Biden Jr. is an American politician who is the 46th