import whisper
from enum import Enum

class ModelType(Enum):
    TINY = 'tiny'
    BASE = 'base'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'

class ASR:
    def __init__(self, model_type: ModelType = ModelType.BASE):
        self.model = whisper.load_model(model_type.value)
    
    def transcribe(self, audio_file):
        return self.model.transcribe(audio_file, fp16=False)['text']