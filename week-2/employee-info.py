"""
Week 2 - Activity 7 : Develop a basic HR project using OO - Due date 15.8.25, 11:59 PM
You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information,
including each employee’s name, salary, and job title.
Requirements:
Create at least two Employee objects with different data.
Call the display_info() method to show each employee’s details.
Call the give_raise() method to increase an employee’s salary and display the updated amount.
"""


class Employee:
    def __init__(self,employee):
        self.employee_detail = employee
    
    def display_info(self):
        print(f'Id: {self.employee_detail['id']}, Name: {self.employee_detail['name']}, Salary: {self.employee_detail['salary']}, Job Title: {self.employee_detail['job_title']}\n')

    def give_raise(self,amount):
        self.employee_detail['salary'] += amount
        print(f"{self.employee_detail['name']}'s salary is raised by ${amount}. New salary: ${self.employee_detail['salary']}")
        
        
    
        
def main():
    all_employees = [
        Employee({"id":1,'name':'Sham','salary':500,'job_title':'CEO'}),
        Employee({"id":2,'name':'Aasish','salary':100,'job_title':'SDE'}),
    ]
    
    for index,employee in enumerate(all_employees):
        print(f"\n******* Employee {index+1} ******")
        employee.display_info()
        
    while True:
        try:
            emp_id = input("Enter the id of the employee if you want to give a raise (or 'q' to Quit):")
            if emp_id.lower() == 'q':
                print("Thank you!.")
                break
            emp_id = int(emp_id)
            valid_employee = next((e for e in all_employees if e.employee_detail['id'] == emp_id), None)
            
            if not valid_employee:
                print("Employee doesn't exist in the system, please try altering search criteria.\n")
                continue
            
            if(valid_employee):
                raise_amount = float(input(f"Enter raise amount for {valid_employee.employee_detail['name']}: "))
                if raise_amount <= 0:
                    print("Oooops! Raise amount must be a positive number.\n")
                    continue
                valid_employee.give_raise(raise_amount)
                
        except ValueError:
             print("Invalid input. Please enter a valid one.")
            
        
        
        
    
if __name__ == "__main__":
    main()