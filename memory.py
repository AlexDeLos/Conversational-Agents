#storing and retreiving files from memory
from ast import keyword


class long_term_mem:
    def __init__(self,keyword, emotion_array):
        self.keyword = keyword
        self.emotion = emotion_array


def store_to_long_term(list: list[long_term_mem]):
    for mem in list:
        mem.emotion.add()
    print("storing to long term")