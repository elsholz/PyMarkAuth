class List:
    def __init__(self, *args):
        self.elements = []

        for a in args:
            self.elements.append(ListElement(prefix=self.prefix, item=a))

    def __str__(self):
        return '\n'.join(str(x) for x in self.elements)

class ListElement:
    def __init__(self, prefix, item):
        self.prefix = prefix
        self.item = item

    def __str__(self):
        return self.prefix + str(self.item)


class OrderedList(List):
    def __init__(self, *args):
        self.prefix = '1. '
        super().__init__(*args)

class UnorderedList(List):
    def __init__(self, *args):
        self.prefix = '- '
        super().__init__(*args)
