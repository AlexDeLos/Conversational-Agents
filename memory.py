#storing and retreiving files from memory
from ast import keyword
import networkx as nx


class long_term_mem:
    def __init__(self,keyword, emotion_array):
        self.keyword = keyword
        self.emotion = emotion_array

class memory:
    def __init__(self, userName):
        try:
            with open("memoryStore/" + userName) as jsonFile:
                self.long_term = json.load(jsonFile)
                jsonFile.close()
        except IOError:
            self.long_term = nx.Graph() #this still needs saving
        self.short_term = []

    def process_input_to_mem(list_of_key_words: list[long_term_mem]):
        
def build_memory_graph():
    G = nx.Graph()
def add_to_memory(keyword_dict):
    i = 0
    for key in keyword_dict:
        G.add_node(i, key = key, emotion = keyword_dict[key])
        i += 1
