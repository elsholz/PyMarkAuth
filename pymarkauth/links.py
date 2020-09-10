class Link:
    def __init__(self, target='', display_text=''):
        self.target = target
        self.display_text = display_text or target

    def __str__(self):
        return '\n[' + str(self.display_text) + '](' + str(self.display_text) + ')\n'


class Image:
    def __init__(self, source='', alt_text=''):
        self.source = source
        self.alt_text = alt_text

    def __str__(self):
        return '\n![' + str(self.alt_text) + '](' + str(self.source) + ')\n'
