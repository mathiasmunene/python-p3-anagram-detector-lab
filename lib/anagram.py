# your code goes here!
# lib/anagram.py
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, possible_anagrams):
        return [
            candidate for candidate in possible_anagrams
            if sorted(candidate.lower()) == sorted(self.word)
            and candidate.lower() != self.word
        ]
