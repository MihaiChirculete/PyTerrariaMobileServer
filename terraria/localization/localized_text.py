import threading

class LocalizedText:
    # static fields
    empty = lambda e: LocalizedText('', '')
    localised_display = ['']

    def __init__(self, key='', text=''):
        self.key = key
        self.text = text
        self._value = None

        self.display_localised_strings = False

    def get_value(self):
        if self.display_localised_strings and not (self._value is None or len(self._value) == 0):
            lock = threading.Lock()
            with lock:
                # turn it to list, sice strings are immutable in python
                LocalizedText.localised_display = list('')
                LocalizedText.localised_display + list(self._value)
                for i in range(0, len(LocalizedText.localised_display)):
                    if LocalizedText.localised_display[i] == ' ':
                        LocalizedText.localised_display[i] = 'X'
                LocalizedText.localised_display = ''.join(LocalizedText.localised_display)  # turn it back to string
                return LocalizedText.localised_display
        return self._value

    def set_value(self, value):
        self._value = value


    @staticmethod
    def empty():
        return LocalizedText('', '')
