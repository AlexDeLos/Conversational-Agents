import os
import shutil
import time

from keyWordExtraction import *
from memory import *
from chatbot import *
from furhat_remote_api import FurhatRemoteAPI
from input.ser import extract_feature
import sounddevice as sd
import pickle, uuid
from scipy.io.wavfile import write


def zipIntoDic(test_keys, value):
    res = {}
    for key in test_keys:
        res[key] = value
    return res
if os.path.exists('tmp'):
        shutil.rmtree('tmp')
        os.makedirs('tmp')
ser = pickle.load(open("input/result/mlp_classifier.model", "rb"))

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
print("Username is", userName)
mem = Memory(userName)
chatbot = Chatbot(userName, 'Matthew')
# print(nameResponse.message)
textInput ="NO"
end = False
wav_file = f'tmp/{str(uuid.uuid4())}.wav'
while not end:
    response = furhat.listen()
    print("listen")
    if response.success:
        textInput = response.message
        #print(textInput)

        keyWords = get_key_concepts(textInput)
        print(keyWords)
        if textInput == "okay we are done":
            print("ending")
            mem.end_convo()
            end=True
            break

        myrecording = sd.rec(int(3*16000), samplerate=16000, channels=1, dtype="float32")
        sd.wait()   
        write(wav_file, 16000, myrecording)
        emotion = ser.predict_proba(extract_feature(wav_file, mfcc = True, chroma = True, mel = True).reshape(1,-1))[0]
        print(emotion)

        dic = zipIntoDic(keyWords,emotion)
        mem.add_to_memory(dic)
        appended = mem.get_mem(dic)
        for word in appended:
            dic[word] = emotion
            break
        print(textInput)
        response = chatbot.talk(textInput, dic)
        print(response)
        furhat.say(text=response)
        print("done")
    else:
        mem.end_convo()
        end=True
