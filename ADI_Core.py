from pynput import keyboard
import speech_recognition as sr
import pyaudio

from TTS import _TTS
from constants import KEYWORDS, MODULES


class ADI:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speak("Witaj, żeby mnie wywołać naciśnij num 0")

    def listen(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            result = self.recognizer.recognize_google(audio, "pl-PL")
            result = result.lower()
        return result

    def speak(self, text):
        tts = _TTS()
        tts.start(text)
        del tts

    def next_request(self):
        self.speak("Pomóc w czymś jeszcze?")
        cont = self.listen()
        for n in range(5):
            if "tak" in cont:
                return True
            elif "nie" in cont:
                self.speak("Dobrze")
                return False
            self.speak("Możesz powtórzyć?")
        else:
            self.speak("Nie rozumiem odpowiedzi, kończę działanie")
            return False

    def start_processing(self):
        repeat = True
        while repeat == True:
            self.speak("Słucham")
            stt = self.listen()
            result = self.match_query(stt)
            if len(result):
                self.speak(result)
                repeat = self.next_request()

    def match_query(self, stt):
        for key, item in KEYWORDS:
            if key in stt:
                return MODULES[item].search(stt, key)
        self.speak("Nie rozumiem, musisz powtórzyć")
        return ""
