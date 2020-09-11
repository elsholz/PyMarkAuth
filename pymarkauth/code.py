class Code:
    def __init__(self, *args, inline=False, language=''):
        self.lines = args
        self.language = language
        self.inline = inline

    def __str__(self):
        if self.inline:
            return '`' + '\n'.join(self.lines) + '`'
        else:
            return '\n```' + self.language + '\n' + '\n'.join(self.lines) + '\n```\n'
