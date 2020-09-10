class Lines:
    def __init__(self, *args):
        c = ['\n']
        for arg in args:
            c.extend(['\n', arg])
        c.extend(['\n'])

        self.elements = c

    def __str__(self):
        return ''.join(str(x) for x in self.elements)


class Paragraphs:
    def __init__(self, *args):
        c = ['\n']
        for arg in args:
            c.extend(['\n\n', arg])
        c.extend(['\n'])

        self.elements = c

    def __str__(self):
        return ''.join(str(x) for x in self.elements)


class BlankSeparated:
    def __init__(self, *args):
        self.elements = args

    def __str__(self):
        return ' '.join(str(x) for x in self.elements)
