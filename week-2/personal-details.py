class PersonalDetail:
    def __init__(self):
        self.personal_details = []
    
    def print_infos(self):
        print(f'Name: {self.personal_details[0]}')
        print(f'Age: {self.personal_details[1]}')
        print(f'Address: {self.personal_details[2]}\n')
        
    def get_user_info(self):
        name = input('\nPlease enter name:')
        self.personal_details.append(name)
        age = input('Please enter age:')
        self.personal_details.append(int(age))
        address = input('Please enter address:')
        self.personal_details.append(address)
        
        print('Confirming infos:\n')
            
        self.print_infos()
        
    def display_infos(self):
        age_to_add = input('How many years do you want to add to your age:')
        self.personal_details[1] += int(age_to_add)
        print('\nThanks for the update, your new info is:')  
        print(f'{self.personal_details[0]} aged {self.personal_details[1]} living in {self.personal_details[2]}\n')
             
        
        

person1 = PersonalDetail()
person1.get_user_info()
person1.display_infos()