# code adapted from: https://www.thepythoncode.com/article/building-a-speech-emotion-recognizer-using-sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

import os
import pickle
import soundfile
import numpy as np
import librosa
import glob
import os
from sklearn.model_selection import train_test_split

# all emotions on RAVDESS dataset
int2emotion = {
    "01": "neutral",
    "02": "calm",
    "03": "happy",
    "04": "sad",
    "05": "angry",
    "06": "fearful",
    "07": "disgust",
    "08": "surprised"
}

#all emotions used in the trained model
EMOTIONS = {
    "angry",
    "sad",
    "neutral",
    "happy"
}

def extract_feature(file_name, mfcc = False, chroma = False, mel = False, contrast = False, tonnetz = False):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        if chroma or contrast:
            stft = np.abs(librosa.stft(X))
        result = np.array([])

        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result = np.hstack((result, mfccs))

        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result = np.hstack((result, chroma))

        if mel:
            mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T,axis=0)
            result = np.hstack((result, mel))

        if contrast:
            contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
            result = np.hstack((result, contrast))

        if tonnetz:
            tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
            result = np.hstack((result, tonnetz))

    return result


def load_data(test_size=0.2):
    X, y = [], []
    for file in glob.glob("data/Actor_*/*.wav"):
        basename = os.path.basename(file)

        emotion = int2emotion[basename.split("-")[2]]
        if emotion not in EMOTIONS:
            continue
        
        features = extract_feature(file, mfcc=True, chroma=True, mel=True)
        X.append(features)
        y.append(emotion)

    return train_test_split(np.array(X), y, test_size=test_size, random_state=7)


def train_ser_model():
    X_train, X_test, y_train, y_test = load_data(test_size=0.25)

    print("[+] Number of training samples:", X_train.shape[0])
    print("[+] Number of testing samples:", X_test.shape[0])
    print("[+] Number of features:", X_train.shape[1])

    model_params = {
        'alpha': 0.01,
        'batch_size': 256,
        'epsilon': 1e-08, 
        'hidden_layer_sizes': (300,), 
        'learning_rate': 'adaptive', 
        'max_iter': 500, 
    }
    model = MLPClassifier(**model_params)

    print("[*] Training the model...")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)

    print("Accuracy: {:.2f}%".format(accuracy*100))

    if not os.path.isdir("result"):
        os.mkdir("result")

    pickle.dump(model, open("result/mlp_classifier.model", "wb"))