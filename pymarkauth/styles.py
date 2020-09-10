class Bold:
    def __init__(self, *args):
        self.elements = args

    def __str__(self):
        return '**' + '** **'.join(str(x) for x in self.elements) + '**'


class Italics:
    def __init__(self, *args):
        self.elements = args

    def __str__(self):
        return '_' + '_ _'.join(str(x) for x in self.elements) + '_'


class StrikeThrough:
    def __init__(self, *args):
        self.elements = args

    def __str__(self):
        return '~~' + '~~ ~~'.join(str(x) for x in self.elements) + '~~'
