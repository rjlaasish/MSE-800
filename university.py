
# Base Class
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")
    
# Subclass
class Staff:
    def __init__(self):
        pass

# Student inherits Person Attrs.
class Student(Person): 
    def __init__(self):
        pass
    
# General Staff inherits both Person (like name, address, age) and Staff Attrs. (tax code, department)
class GeneralStaff(Person, Staff):
    def __init__(self):
        pass
    
# Academic Staff inherits both Person (like name, address, age) and Staff Attrs. (tax code, department)
class AcademicsStaff(Person, Staff):
    def __init__(self):
        pass
