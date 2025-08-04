import numpy as np

temperature = [18.5, 19, 20, 25.0, 2, 30, 13.9]

average_temp= np.mean(temperature)


# F = C × 9/5 + 32
def convert_to_fahrenheit():
    print(temperature)
    print('*** Conversion to fahrenheit: ***',end='\n')
    for t in temperature:
        in_fahrenheit = t * 9/5 + 32
        print(f"{t} converted {in_fahrenheit} in fahrenheit")
    print('\n')
        
convert_to_fahrenheit()

print(f"Average temperature is: {average_temp}",end="\n\n")
print(f"Highest temperature is: {np.max(temperature)}",end="\n")
print(f"Lowest temperature is: {np.min(temperature)}",end="\n")

def find_indices():
    print('\n')
    for index, item in enumerate(temperature):
        if(item > 20):
            print(f"Item greater than 20 is in {index} index and item is {item}.")
        
find_indices()
    
