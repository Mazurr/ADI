import pyttsx3


class _TTS:

    engine = None
    rate = None

    def __init__(self):
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty("rate")
        self.engine.setProperty("rate", rate - 60)

    def start(self, text_):
        self.engine.say(text_)
        self.engine.runAndWait()
