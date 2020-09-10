class List:
    def __init__(self, items=None, prefix=None, level=0):
        self.prefix = prefix
        self.items = []
        self.level = level

        if isinstance(items, list):
            # contains list of elements

            for el in items:
                if isinstance(el, list):
                    self.items.append(List(items=el, prefix=self.prefix, level=self.level + 1))
                elif isinstance(el, List):
                    self.items.append(el)
                    el.level = self.level
                else:
                    self.items.append(ListItem(content=el, level=self.level, prefix=self.prefix))

        else:
            raise ValueError("`items` must be list.")

    def __str__(self):
        return '\n'.join(str(x) for x in self.items)

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level
        for el in self.items:
            el.level = self.__level + 1


class ListItem:
    def __init__(self, content, prefix, level=0):
        self.content = content
        self.prefix = prefix
        self.level = level

    def __str__(self):
        return '    ' * self.level + self.prefix + str(self.content)


class OrderedList(List):
    def __init__(self, items):
        self.prefix = '1. '
        super().__init__(items=items, prefix=self.prefix)


class UnorderedList(List):
    def __init__(self, items):
        self.prefix = '- '
        super().__init__(items=items, prefix=self.prefix)
