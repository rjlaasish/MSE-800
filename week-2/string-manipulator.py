class StringManipulator:
    def __init__(self,text):
        self.text = text
        
    def get_index(self,char):
        return self.text.find(char)
    
    def transform_uppercase(self,char):
        return char.upper()
    
    def find_length(self, char):
        return len(char)
    
    
word= 'example'
letter_to_find = 'p'
name = StringManipulator(word)
print(f'\n{letter_to_find} is in {name.get_index(letter_to_find)} index')
print(f'Uppercase of the string is {name.transform_uppercase(word)}')
print(f'Length of the string is {name.find_length(word)}\n')