class Student:
    def __init__(self, name, age):
        self.name = name # public​
        self._age = age # protected​
        self.__grade = 'A' # private​

    def get_grade(self):
        return self.__grade
    
    def display_grade(self):
        return f"{self.name} has achieved grade {self.__grade}."
    
s = Student('Ali', 20)
print(s.name) 
print(s._age) 
print(s.get_grade()) 
print(s.display_grade())
    
    

    
class Database:
    def __init__(self, db_name, user, password):
        self.db_name = db_name        
        self._user = user             # Protected attribute 
        self.__password = password    # Private attribute
        
        
    def show_info(self):
        print(f"Database: {self.db_name}")
        print(f"User: {self._user}")
        # Can't directly print __password here outside the class, but we can inside
        print(f"Password: {self.__password}")

        





db = Database("TestDB", "admin", "s3cr3t")

print(db.db_name)     # Public - accessible
print(db._user)     # Protected - accessible but not recommended this way
# print(db.__password)  # Error! Private attribute, can't access directly

