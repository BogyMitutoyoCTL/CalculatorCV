import keyboard
import multiprocessing


class KeyListener:
    def __init__(self):
        self.setter = None

    def on_keypress(self, key: str) -> None:
        if key == 'esc':
            key = -1
        key = int(key)
        self.setter.put(key)

    def listen(self):
        self.create_hotkey('0')
        self.create_hotkey('1')
        self.create_hotkey('2')
        self.create_hotkey('3')
        self.create_hotkey('4')
        self.create_hotkey('6')
        self.create_hotkey('7')
        self.create_hotkey('esc')
        keyboard.wait('esc')

    def create_hotkey(self, key: str) -> None:
        keyboard.add_hotkey(key, self.on_keypress, key)

    def start(self, queue: multiprocessing.Queue) -> None:
        self.setter = queue
        self.listen()

