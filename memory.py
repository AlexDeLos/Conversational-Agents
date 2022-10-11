#storing and retreiving files from memory
from ast import keyword
import networkx as nx
import json
class memory:
    def __init__(self, userName):
        try:
            with open("memoryStore/" + userName) as jsonFile:
                self.long_term = json.load(jsonFile)
                jsonFile.close()
        except IOError:
            self.long_term = nx.Graph() #this still needs saving
        self.short_term = []

    # def process_input_to_mem(list_of_key_words: list[long_term_mem]):

# def build_memory_graph():
#     G = nx.Graph()
    def add_to_memory(self, keyword_dict):
        i = 0
        for key in keyword_dict:
            # check if the word is in graph
            # add it or fuse it
            # add the new connections
            self.long_term.add_node(i, key = key, emotion = keyword_dict[key])
            i += 1

