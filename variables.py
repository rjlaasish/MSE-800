factorial_number = input("Enter a number to calculate its factorial: ")



# use while loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
    
    

    
print(factorial(int(factorial_number)))