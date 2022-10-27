from input.recorder import Recorder
from multiprocessing import Queue, Process
from furhat_remote_api import FurhatRemoteAPI
from input.ser import extract_feature
import sounddevice as sd
import pickle, uuid
import soundfile as sf
from scipy.io.wavfile import write

def main():
    # data_queue = Queue()
    # recorder = Recorder(data_queue)
    # recorder.start()

    ser = pickle.load(open("input/result/mlp_classifier.model", "rb"))

    furhat = FurhatRemoteAPI("localhost")

    # Get the voices on the robot
    # voices = furhat.get_voices()

    # Set the voice of the robot
    furhat.set_voice(name='Matthew')

    # Say "Hi there!"
    furhat.say(text="Hi there!Please state your name.")
    name = furhat.listen()
    print(name.message)
    furhat.say(text="Thank you! What do you want to talk about?")
    wav_file = f'tmp/{str(uuid.uuid4())}.wav'

    while True:
        
        result = furhat.listen()
        print(result.message)

        myrecording = sd.rec(int(3*16000), samplerate=16000, channels=1, dtype="float32")
        sd.wait()   
        write(wav_file, 16000, myrecording)
        emotion = ser.predict_proba(extract_feature(wav_file, mfcc = True, chroma = True, mel = True).reshape(1,-1))  
        furhat.say(wav_file)

        print(emotion)
        furhat.say(text = "Can you please repeat that?")
    
if __name__ == "__main__":
    main()