from keyWordExtraction import *
from memory import *
from furhat_remote_api import FurhatRemoteAPI
from chatbot import *


def zipIntoDic(test_keys, value):
    res = {}
    for key in test_keys:
        res[key] = value
    return res


# Create an instance of the FurhatRemoteAPI class, providing the address of the robot or the SDK running the virtual robot
furhat = FurhatRemoteAPI("localhost")

# Get the voices on the robot
voices = furhat.get_voices()

# Set the voice of the robot
furhat.set_voice(name='Matthew')

# Say "Hi there!"
furhat.say(text="Hi there!, State your name")

nameResponse = furhat.listen()


furhat.say(text="Great! What do you need?")


userName = nameResponse.message
mem= Memory(userName)
chatbot = Chatbot(userName, 'Matthew')
print(nameResponse.message)
textInput ="NO"
end = False
while not end:
    response = furhat.listen()
    if response.success:
        textInput = response.message
        keyWords = get_key_concepts(textInput)
        #print(keyWords)
        dic = zipIntoDic(keyWords,[0.5,0.5,0.5,0.5])
        furhat.say(text=chatbot.talk(textInput, dic))
        mem.add_to_memory(dic)
        print("done")
    else:
        mem.end_convo()
        end=True