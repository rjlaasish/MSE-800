# week1- activity 3: Rainfall Analysis with NumPy
# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
#
# Tasks:
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Calculate the 75th percentile of the rainfall data and identify values above it. (help : use numpy.percentile())


import numpy as np
import calendar

wk_rainfall= [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
np_array = np.array(wk_rainfall)
days = list(calendar.day_name)  # it starts from Monday

# Adjust to start from Sunday
days = days[-1:] + days[:-1]
days = np.array(days)

if __name__ == "__main__":

    # To nparray
    print(f"To np array: {np_array}")

    # Total rainfall for week
    print(f"Total wk rainfall: {np.sum(np_array):.2f}")

    # Average rainfall
    print(f"Average rainfall: {np.average(np_array):.2f}")

    # Days with no rain
    print(f"Days with no rainfall: {np.count_nonzero(np_array==0)} days")

    # Days with more than 5mm rain
    indices = np.where(np_array > 5)[0]
    print(f"Days with more than 5mm rain fall: {days[indices]} ({indices})")

    # 75th percentile
    print(np_array)
    percentile_75 = np.percentile(np_array, 75)
    values_above_75 = np_array[np_array > percentile_75]

    print("75th percentile:", percentile_75)
    print("Values above 75th percentile:", values_above_75)