class CountWord:
    def __init__(self, sentence):
        self.sentence = sentence
        
    def count_word(self):
        return len(self.sentence.strip().split(" "))
    
    
    
sentence = input('\nPlease enter the sentence:\n')
c_word = CountWord(sentence)

print('Total words:',c_word.count_word())