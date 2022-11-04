#central file
from furhat_remote_api import FurhatRemoteAPI


from keyWordExtraction import *
from memory import *
import furhat_remote_api #import FurhatRemoteAPI

def main():
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

    print(nameResponse.message)
    textInput ="NO"
    end = False
    while not end:
        response = furhat.listen()
        if response.success:
            textInput = response.message
    keyWords = get_key_concepts(textInput)

    print(keyWords)
    emotions = []
    #need to zip the key words and vector BOTH NEED TO HAVE THE SAME LENGTH
    dictionary = zipIntoDic(keyWords,emotions)
    mem = Memory(userName)


def zipIntoDic(test_keys, value):
    res = {}
    for key in test_keys:
        res[key] = value
    return res

if __name__ == "__main__":
    main()