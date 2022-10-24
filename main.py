#central file

from keyWordExtraction import *
from memory import *
import furhat_remote_api #import FurhatRemoteAPI

def main():
    userName = "John"
    textInput ="test input"

    keyWords = get_key_concepts(textInput)

    emotions = []
    #need to zip the key words and vector BOTH NEED TO HAVE THE SAME LENGTH
    dictionary = zipIntoDic(keyWords,emotions)
    mem = Memory(userName)
    mem.add_to_memory(dictionary)
    #mem.get_mem("test", [1,1,1,1])
    mem.end_convo()


def zipIntoDic(test_keys, test_values):
    res = {}
    for key in test_keys:
        for value in test_values:
            res[key] = value
            test_values.remove(value)
            break
    return res
if __name__ == "__main__":
    main()