# Develop a Python project to perform the following tasks (import NumPy as np):
# 1. Calculate and print the average temperature for the week using NumPy.
#       Temperature data (in °C): [18.5, 19, 20, 25.0, 2, 30, 13.9]
# 2. Determine and display the highest and lowest recorded temperatures.
# 3. Convert all temperatures to Fahrenheit and print the converted values.
#       (Use the formula: F = C × 9/5 + 32)
# 4. Identify and print the indices of days where the temperature exceeded 20°C.

import numpy as np

temperatures = [18.5, 19, 20, 25.0, 2, 30, 13.9]


if __name__ == "__main__":
    # Average Temperature
    print(f"\nAverage temperature is {np.mean(temperatures):.2f}", end='\n\n')

    # Highest Temperature
    print(f"Highest temperature is {np.max(temperatures):.2f}",end='\n\n')

    # Lowest Temperature
    print(f"Lowest temperature is {np.min(temperatures):.2f}",end='\n\n')

    # Convert to fahrenheit
    print('Converted temperatures to fahrenheit:', end='\n')
    for index, item in enumerate(temperatures):
        print(f"{temperatures[index]}°C → {item * 9/5 + 32}°F")
    print('\n')

    # Days exceeding 20°C
    temp_exceeding_index= np.where(np.array(temperatures) > 20)[0]
    print('Indices of days exceeding 20°C :\n')
    for item in temp_exceeding_index:
        print(f"{temperatures[item]}°C ({item + 1})", end='\n')
