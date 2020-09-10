from .lists import UnorderedList, OrderedList
from .styles import Italics, Bold, StrikeThrough
from .lines import Lines, Paragraphs, BlankSeparated
from .links import Link, Image
from .tables import Table


class MarkDown:
    def __init__(self, file_path=None):
        self._content = []
        self.is_root = True
        self.level = 0
        self.file_path = file_path

    def __enter__(self):
        self.output_file = open(self.file_path, 'w') if self.file_path else None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.output_file:
            self.output_file.write(self.__str__())
            self.output_file.close()

    def __str__(self):
        """Generate markdown"""
        return ''.join(str(x) for x in self._content)

    def section(self, title):
        """Generates a subsection from a section"""
        s = Section(title, level=self.level + 1)
        self._content.append(s)
        return s

    def text(self, *args):
        """Return a Text Object"""
        c = Text(*args)
        return c if self.is_root else self._content.append(c)

    def newline(self):
        """Insert a line break"""
        c = '\n'
        return c if self.is_root else self._content.append(c)

    def empty_line(self):
        """Insert empty line"""
        c = '\n\n'
        return c if self.is_root else self._content.append(c)

    def lines(self, *args):
        """Stick arguments together, with a new line in between"""
        c = Lines(*args)
        return c if self.is_root else self._content.append(c)

    def paragraphs(self, *args):
        """Stick arguments together, with a new line in between"""
        c = Paragraphs(*args)
        return c if self.is_root else self._content.append(c)

    def blank_separated(self, *args):
        """Separate each item with one space in between."""
        c = BlankSeparated(*args)
        return c if self.is_root else self._content.append(c)

    def italics(self, *args):
        """Apply styling to all text items"""
        c = Italics(*args)
        return c if self.is_root else self._content.append(c)

    def bold(self, *args):
        """Apply styling to all arguments"""
        c = Bold(*args)
        return c if self.is_root else self._content.append(c)

    def strike_through(self, *args):
        """Apply styling to all arguments"""
        c = StrikeThrough(*args)
        return c if self.is_root else self._content.append(c)

    def unordered_list(self, *args):
        """Make unordered list from items"""
        c = UnorderedList(*args)
        return c if self.is_root else self._content.append(c)

    def ordered_list(self, *args):
        """Make ordered list from items"""
        c = OrderedList(*args)
        return c if self.is_root else self._content.append(c)


class Section(MarkDown):
    def __init__(self, title, level):
        self.title = title
        self.level = level if level <= 6 else 6
        self._content = []
        self.is_root = False

    def __str__(self):
        return '\n\n' + "#" * self.level + " " + str(self.title) + '\n' + ''.join(str(x) for x in self._content)


class Text:
    def __init__(self, *args):
        self.elements = args

    def __str__(self):
        return ''.join(str(x) for x in self.elements)
