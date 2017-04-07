import keyboard
import multiprocessing


class KeyListener:
    def __init__(self):
        self.setter = None

    def on_keypress(self, key: str) -> None:
        if key == 'x':
            key = -1
        key = int(key)
        self.setter.put(key)

    def listen(self) -> None:
        for key in ['0', '1', '2', '3', '4', '6', '7']:
            self.register_hotkey(key)
        keyboard.add_hotkey('esc', self.on_keypress, 'x')
        keyboard.wait('esc')

    def register_hotkey(self, key: str) -> None:
        keyboard.add_hotkey(key, self.on_keypress, key)

    def start(self, queue: multiprocessing.Queue) -> None:
        self.setter = queue
        self.listen()

