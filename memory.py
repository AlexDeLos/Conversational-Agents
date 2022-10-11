#storing and retreiving files from memory
import itertools
from ast import keyword
import networkx as nx
import json
import numpy as np
from networkx.readwrite import json_graph
class Memory:
    def __init__(self, userName):
        self.user_name = userName
        try:
            with open("memoryStore/" + userName+ '.json') as jsonFile:
                data = json.load(jsonFile)
                self.long_term = json_graph.node_link_graph(data)
                print(self.long_term.nodes.data())
                jsonFile.close()
        except IOError:
            self.long_term = nx.Graph() #this still needs saving
        self.short_term = []

    # def process_input_to_mem(list_of_key_words: list[long_term_mem]):

# def build_memory_graph():
#     G = nx.Graph()
    def add_to_memory(self, keyword_dict):
        for key in keyword_dict:
            # check if the word is in graph
            try:
                current = np.array(self.long_term.nodes[key]['emotion'])
                new = np.array(keyword_dict[key])
                avg = (current + new) / 2
                # print(avg)
                self.long_term.add_node(key, emotion = list(avg))

            except KeyError:
                self.long_term.add_node(key, emotion=keyword_dict[key])
                # add strength to the edge when mentioned multiple times together (also in nodes)
                self.long_term.add_edges_from(itertools.combinations(keyword_dict.keys(), 2))
            # add it or fuse it
            # add the new connections
            # print(self.long_term.nodes.data())
    def end_convo (self):
        with open("memoryStore/" + self.user_name + '.json', 'w') as jsonFile:
            data = json_graph.node_link_data(self.long_term)
            json.dump(data ,jsonFile)
            jsonFile.close()


mem = Memory('John')
mem.add_to_memory ({'like': [1,1,1] ,'dog': [0.5,0.1,0.9]})
mem.add_to_memory ({'dog': [0.9,0.1,0.9]})
mem.add_to_memory ({'like': [0.1,0.1,0.1]})
mem.add_to_memory ({'eleni': [0.4,0.7,0.1], 'like': [0.1,0.1,0.1]})
# print(mem.long_term.nodes.data())
# print(mem.long_term.edges.data())

mem.end_convo()
