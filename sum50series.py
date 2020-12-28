# Program to print the sum of series from 1,2,3,......up to 50th term
# Programmed by Rudransh Joshi
# Class: XI - A (Second Shift)

import os # Just to clear the garbage data in from the terminal
os.system("cls") # Just to clear the garbage data in from the terminal


num = 50
sum_list = []  # Initialising Empty List
for i in range(1, num + 1): # Appending all numbers from 1 to 50 in a list and summing it up
    sum_list.append(i)
print(f"The sum of series 1,2,3,...50 is:\t{sum(sum_list)}")    



'''
Alternate Way: Using Formula "n * (n + 1) / 2"
num = 50
result = int(num * (num + 1) / 2)
print(f"The sum of series 1,2,3,...50 is:\t{result}")
'''