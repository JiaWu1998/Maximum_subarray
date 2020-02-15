 # Jiaxing Wu 
# Seat: 63
# A20398273

# Yik Yu Lau
# Seat 37
# A20397022

# Problem: Given an a list of random numbers, each number represents the price
# of stocks at a given day, which is represented by the index of the numbers in 
# that array. Find the pair of buy and sell date that will make the most net 
# profit.   
# 
# Rule 1: Buy one unit of stock only one time
# Rule 2: Sell one stock on a later date
# Rule 3: You are allowed to have the knowledge of the prices of stocks in all given days
 
import random

buy_sell_pair = [-1,-1]
curr_profit = 0
array = [random.randint(0,101) for _ in range(10)]

loops = 0

for i in range(len(array)):
    for j in range(i,len(array)):
        temp = array[j] - array[i]
        if curr_profit < temp:
            curr_profit = temp
            buy_sell_pair = [i,j]
        loops += 1

print(f"Buy at day {buy_sell_pair[0]+1} and sell at day {buy_sell_pair[1]+1}.\
    \nYour profit is ${curr_profit}")

print(f"\nNumbers of Loops: {loops}")