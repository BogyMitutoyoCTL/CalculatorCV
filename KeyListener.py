import keyboard


class KeyListener:
    def __init__(self):
        self.setter = None

    def action(self, key):
        if key == '9':
            key = -1
        key = int(key)
        self.setter.put(key)

    def listen(self):
        keyboard.add_hotkey('0', self.action, '0')
        keyboard.add_hotkey('1', self.action, '1')
        keyboard.add_hotkey('2', self.action, '2')
        keyboard.add_hotkey('3', self.action, '3')
        keyboard.add_hotkey('4', self.action, '4')
        keyboard.add_hotkey('5', self.action, '5')
        keyboard.add_hotkey('6', self.action, '6')
        keyboard.add_hotkey('7', self.action, '7')
        keyboard.add_hotkey('esc', self.action, '9')
        keyboard.wait('esc')

    def start(self, q):
        self.setter = q
        self.listen()

