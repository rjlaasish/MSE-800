class StringManipulator:
    def __init__(self,text):
        self.text = text
        
    def get_index(self,char):
        return self.text.find(char)
    
    def transform_uppercase(self):
        return self.text.upper()
    
    def find_length(self):
        return len(self.text)
    
    def reverse_string(self):
        return self.text[::-1]
    
    def slice_string(self,index):
        return self.text[0:index]
    
    def is_palindrome(self):
        return self.text == self.text[::-1]
    
    def count_character(self):
        char_frequency = {}
        for char in self.text:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        return char_frequency
    
    def remove_duplicates(self):
        chars = set()
        for char in self.text:
           chars.add(char)

        return chars
            
            
            
    
    
word= 'madam'
letter_to_find = 'p'
name = StringManipulator(word)

print(f'\n{letter_to_find} is in {name.get_index(letter_to_find)} index')
print(f'Uppercase of the string is {name.transform_uppercase()}')
print(f'Length of the string is {name.find_length()}')
print(f'Reversed string: {name.reverse_string()}')
print(f'String sliced at 4th index: {name.slice_string(4)}')
print(f'Is palindrome number? : {name.is_palindrome() }')
print(f'Count of the character : {name.count_character() }')
print(f'Duplicates removed : {name.remove_duplicates() }')


print(f'{3==3}')


print('\n')