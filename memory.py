#storing and retreiving files from memory
import itertools
import numpy as np
from scipy import spatial
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
                jsonFile.close()
        except IOError:
            self.long_term = nx.Graph()
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
                print(current)
                print(new)
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

    #saves the memory we have gathered and saves it in a JSON file unique for the user
    def end_convo (self):
        for node in self.long_term.nodes.data():
            newArray = [x / 1.2 for x in list(node[1]['emotion'])]
            self.long_term.add_node(node[0], emotion = newArray)

        with open("memoryStore/" + self.user_name + '.json', 'w') as jsonFile:
            data = json_graph.node_link_data(self.long_term)
            #print(data)
            json.dump(data ,jsonFile)
            jsonFile.close()
            #print("saved")

    def get_mem (self, dictionary):
        #TODO: implement this you get the closest node to the graph and that has the closes memory vector for each keyword
        #return the array of keywords
        result = []
        for element in dictionary:
            neighbors = list(self.long_term.neighbors(element))
            #print(neighbors)
            for n in neighbors:
                vector = self.long_term.nodes[n]["emotion"]
                similarity = 1 - spatial.distance.cosine(vector, dictionary[element])
                #print(similarity)
                #print(n)
                if (similarity > 0.9):
                    result.append(n)
        # print(result)
        return result

