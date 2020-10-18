import wikipedia
from main import adi


class ADInfo:
    def __init__(self):
        wikipedia.set_lang("pl")

    def search(self, text, key):
        text = self.get_keyword(text, key)
        text = wikipedia.suggest(text)
        result = wikipedia.search(text, results=5)
        if len(result) > 1:
            answer = self.more_then_1(result)
        else:
            answer = wikipedia.summary(result)
        return answer

    def get_keyword(self, text, key):
        cut = text.split(key)
        return cut[1]

    def more_then_1(self, result):
        for n, r in enumerate(result):
            result[n] = str(n + 1) + " " + r
        answer = "Jest parę możliwości " + (", ".join(result))
        for n in range(5):
            number = "1"
            number = adi.listen()
            if number in ("1", "2", "3", "4", "5"):
                answer = wikipedia.summary(result[number])
                break
            adi.speak("Podaj numer od 1 do 5")
        else:
            answer = ""
            adi.speak("Nie rozumiem, spróbuj zadać pytanie jeszcze raz")
        return answer
