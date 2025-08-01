factorial_number = input('\nPlease enter a number to calculate the factorial:')

def factorial(n):
    if(n < 0):
        return 'Number cannot be less than 0'
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        while n > 1:
            result = result * n
            n=n-1
        return result
    
    
try:
    input_value = int(factorial_number)
    print(factorial(input_value), end='\n\n')
except ValueError:
    print('⚠️ Please enter a valid number to calculate the factorial ⚠️',end='\n\n')
    
    