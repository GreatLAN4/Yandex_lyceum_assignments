class MinMaxWordFinder:
    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence):
        for i in sentence.split():
            self.sentences.append(i)

    def shortest_words(self):
        word = []
        if not self.sentences:
            return ""
        len_min_word = len(min(self.sentences, key=len))
        for i in self.sentences:
            if len(i) == len_min_word:
                word.append(i)
        word.sort()

        return word

    def longest_words(self):
        word = []
        if not self.sentences:
            return ""
        len_max_word = len(max(self.sentences, key=len))
        for i in self.sentences:
            if len(i) == len_max_word and i not in word:
                word.append(i)
        word.sort()

        return word
