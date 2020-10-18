from pynput import keyboard
from ADI_Core import ADI

if __name__ == "__main__":
    adi = ADI()

    class MyException(Exception):
        pass

    def execute():
        adi.start_processing()

    def for_canonical(f):
        return lambda k: f(listener.canonical(k))

    def on_release():
        execute()

    hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+<alt>+q"), on_release)

    with keyboard.Listener(
        on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)
    ) as listener:
        try:
            listener.join()
        except MyException as e:
            print("{0} was pressed".format(e.args[0]))
