 # Jiaxing Wu 
# Seat: 63
# A20398273

# Yik Yu Lau
# Seat 37
# A20397022

# Problem: Given an array of integers, find a subarray within all subarrays that 
# has the greatest sum.
# 
# Alternate Explaination:
# Each subarray is given a value that is the sum of all integers in the subarray.
# Find the subarray with the max value. 

 
import random

array = [random.randint(-100,101) for _ in range(100)]
sub_array = []
sum_of_array = 0
loops = 0
ARR_LEN = len(array)

for i in range(ARR_LEN):
    temp_sum = 0
    temp_array = []
    temp_len = ARR_LEN - 1 if i == 0 else ARR_LEN #exludes the whole array because it's not a subarray
    for j in range(i,temp_len): 
        temp_sum += array[j]
        temp_array += [array[j]]
        loops += 1

        if max(sum_of_array, temp_sum) == temp_sum:
            sum_of_array = temp_sum
            sub_array = temp_array

print(f"The max subarray is {sub_array}")
print(f"\nNumbers of Loops: {loops}")