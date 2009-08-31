import random
import sys

class Markov():

    markovtable = {} #defaultdict(list)
    reverse_markovtable = {}
    stopword = "\n"
    w1 = stopword
    w2 = stopword

    stopsentence = (" ", ".", "!", "?","\n",) # Cause a "new sentence" if found at the end of a word
    sentencesep  = "\n" #String used to seperate sentences

    def load_brain(self, text):
        for line in text:
            line = line
            self.add_to_brain(line)
        # Mark the end of the file
        self.markovtable.setdefault( (self.w1, self.w2), [] ).append(self.stopword)        

    def add_to_brain(self, line):
        letters = list(line)
        for letter in letters:
                if letter in self.stopsentence:
                    self.markovtable.setdefault( (self.w1, self.w2), [] ).append(letter)
                    self.w1, self.w2 = self.w2, letter
                    letter = letter
                self.markovtable.setdefault( (self.w1, self.w2), [] ).append(letter)
                self.reverse_markovtable.setdefault( letter, [] ).append((self.w1, self.w2))
                self.w1, self.w2 = self.w2, letter


    def generate_simple_sentence(self, maxsentences=30):
        sentencecount = 0 
        sentence = []
        self.w1 = self.stopword
        self.w2 = self.stopword
        sentences = []
        while sentencecount < maxsentences:
            newword = random.choice(self.markovtable[(self.w1, self.w2)])
            if newword in self.stopsentence:
                sentences.append("".join(sentence))
                sentence = []
                sentencecount += 1
                self.w1 = self.stopword
                self.w2 = self.stopword
            else:
                sentence.append(newword)
            self.w1, self.w2 = self.w2, newword
        return sentences
