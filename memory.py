#storing and retreiving files from memory
from ast import keyword
import networkx as nx


class long_term_mem:
    def __init__(self,keyword, emotion_array):
        self.keyword = keyword
        self.emotion = emotion_array

<<<<<<< main

def store_to_long_term(list: list[long_term_mem]):
    for mem in list:
        mem.emotion.add()
    print("storing to long term")
    print("Eleni is beautiful, Alex sucks! <3")
=======
def build_memory_graph():
    G = nx.Graph()
def add_to_memory(keyword_dict):
    i = 0
    for key in keyword_dict:
        G.add_node(i, key = key, emotion = keyword_dict[key])
        i += 1
>>>>>>> whatever
