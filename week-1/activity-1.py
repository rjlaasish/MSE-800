# Week1- Activity 1: Calculate the Factorial of a Number Using a while Loop
# Develop the first project for MSE800 with using following task:
# Can you write the program using a  while loop?
# What happens if the user enters 0? Try to handle this case in your code.
# Try adding error checking for negative numbers.


print("\n***** Welcome to the Factorial Calculator! *****")

def factorial(x):
    if x < 0:
        return "⚠️  Factorial cannot be calculated for the negative numbers  ⚠️"
    elif 0 <= x <= 1:
        return 1
    else:
        result = 1
        while x > 1:
            result *= x
            x-=1
        return result

if __name__ == "__main__":
    while True:
        try:
            input_number = input("\nPlease enter a number to generate its factorial: ")
            input_value = int(input_number)
            calculated_factorial = factorial(input_value)
            if isinstance(calculated_factorial, str):
                print(calculated_factorial, end='\n\n')
            else:
                print(f"Factorial of {input_value} is {calculated_factorial}.", end='\n\n')
        
        except ValueError:
            print('🔴 Invalid input! Please enter a valid number to calculate the factorial.',end='\n\n')
            
        retry = input("Do you want to calculate another factorial? (yes/no): ").strip().lower()
        if retry not in ['yes', 'y']:
           print("\nThanks for using the Factorial Calculator! Goodbye!\n")
           break