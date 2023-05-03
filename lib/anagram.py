class Anagram:
    def __init__(self, word):
        self.word = sorted([letter for letter in word])
    
    def match(self, anagrams):
        result = []
        for anagram in anagrams:
            if sorted([letter for letter in anagram]) == self.word:
                result.append(anagram)
        return result