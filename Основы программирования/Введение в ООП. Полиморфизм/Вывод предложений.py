class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.paragraph = []

    def add_word(self, word):
        self.paragraph.append(word)

    def end(self):
        row = ''
        for word in self.paragraph:
            if not row:
                row += word
            elif len(row) + len(word) + 1 <= self.width:
                row += ' ' + word
            else:
                print(row)
                row = word
        print(row)
        self.paragraph.clear()


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.paragraph = []

    def add_word(self, word):
        self.paragraph.append(word)

    def end(self):
        row = ''
        for word in self.paragraph:
            if not row:
                row += word
            elif len(row) + len(word) + 1 <= self.width:
                row += ' ' + word
            else:
                print(row.rjust(self.width, ' '))
                row = word
        print(row.rjust(self.width, ' '))
        self.paragraph.clear()
