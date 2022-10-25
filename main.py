#central file

from keyWordExtraction import *
from memory import *
import furhat_remote_api #import FurhatRemoteAPI

def main():
    userName = "John"
    textInput ="Hello, my name is Alex. I am awsome and great at everything"

    keyWords = get_key_concepts(textInput)

    emotions = []
    #need to zip the key words and vector BOTH NEED TO HAVE THE SAME LENGTH
    dictionary = zipIntoDic(keyWords,emotions)
    mem = Memory(userName)
    mem.add_to_memory(dictionary)
    #mem.get_mem("test", [1,1,1,1])
    mem.end_convo()


def zipIntoDic(test_keys, value):
    res = {}
    for key in test_keys:
        res[key] = value
    return res

if __name__ == "__main__":
    main()