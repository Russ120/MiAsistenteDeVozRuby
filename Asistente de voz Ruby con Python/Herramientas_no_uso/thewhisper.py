import whisper
import io
from pydub import audio_segment
import speech_recognition as sr
import tempfile
import os
import pyttsx3


temp_file = tempfile.mktemp()
save_path = os.path.join(temp_file, 'temp.wav')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 145)
engine.setProperty('voice', voices[2].id)


