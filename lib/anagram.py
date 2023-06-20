class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = self._sort_word(word)
    
    def match(self, word_list):
        matches = []
        for word in word_list:
            if self._is_anagram(word):
                matches.append(word)
            else:
                print([])
        return matches
    
    def _sort_word(self, word):
        return ''.join(sorted(word.lower()))
    
    def _is_anagram(self, word):
        return self.sorted_word == self._sort_word(word)
