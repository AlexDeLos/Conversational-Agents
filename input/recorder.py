from time import time
from input.constants import CHANNELS, RMS_THRESHOLD, SAMPLE_RATE, SILENCE_THRESHOLD, TIME_THRESHOLD
from dataclasses import dataclass
from input.asr import ASR, ModelType
from multiprocessing import Process, Queue
from input.ser import extract_feature

import numpy as np
import sounddevice as sd
import soundfile as sf
import os, shutil, uuid
import pickle, time

@dataclass
class RMS:
    time: float
    silent: bool

class Recorder:
    def __init__(self, queue: Queue, model_type: ModelType = ModelType.BASE):
        self.queue = queue
        self.asr = ASR(model_type)
        self.data = []
        self.window = []
        self.ser = pickle.load(open("input/result/mlp_classifier.model", "rb"))

        if os.path.exists('tmp'):
            shutil.rmtree('tmp')
        os.makedirs('tmp')

    def start(self) -> None:
        Process(target=self.record_and_process).start()

    def record_and_process(self) -> None:
        def callback(indata, frames, _time, status) -> None:
            self.last_time = time.time()
            self.data.extend(indata[:, 0])
            self.window.append(RMS(self.last_time, np.sqrt(np.mean(indata[:, 0] ** 2)) < RMS_THRESHOLD))

        self.stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, callback=callback)

        while True:
            self.stream.start()
            self.process_data()
    
    def process_data(self) -> None:
        if not self.window:
            return

        self.window = [ o for o in self.window if (self.last_time - o.time) < TIME_THRESHOLD ]
        percentage_of_silence = sum([ o.silent for o in self.window ]) / len(self.window)

        # Check if there is a silence and there were at least samples for `TIME_THRESHOLD` seconds.
        if percentage_of_silence > SILENCE_THRESHOLD and len(self.window) > 15:
            silent_array = [ o.silent for o in self.window ]
            data = self.data[silent_array.index(False):] if False in silent_array else []

            self.window = []
            self.data = []

            if data:
                Process(target=process_audio_data, args=(self.asr, self.queue, data, self.ser)).start()
    
def process_audio_data(asr: ASR, queue: Queue, data, ser) -> None:
    wav_file = f'tmp/{str(uuid.uuid4())}.wav'
    
    with sf.SoundFile(wav_file, 'w', SAMPLE_RATE, CHANNELS) as file:
        file.write(data)

    text = asr.transcribe(wav_file)

    os.system(f"ffmpeg -i {wav_file} -ac 1 -ar 16000 {wav_file.replace('-', '_')}")
    emotion = ser.predict_proba(extract_feature(wav_file.replace('-', '_'), mfcc = True, chroma = True, mel = True).reshape(1,-1))
    
    queue.put((text, emotion))
    