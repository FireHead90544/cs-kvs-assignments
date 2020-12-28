# Program to print the sum of all odd numbers from 1 to 100
# Programmed by Rudransh Joshi
# Class: XI - A (Second Shift)

import os # Just to clear the garbage data in from the terminal
os.system("cls") # Just to clear the garbage data in from the terminal

num = 100
sum_list = [] # Initialising empty list

for i in range(1, num, 2):   # Using for loop and taking a step of 2 for odd numbers starting from 1 and ending at 100.
    sum_list.append(i)  # Appending all odd numbers from 1 to 100 in a list

print(f"Sum of all odd numbers from 1 to 100 is:\t{sum(sum_list)}")    # Summing up the list and printing the output