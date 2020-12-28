# Program to print the sum of all even numbers from 1 to 100
# Programmed by Rudransh Joshi
# Class: XI - A (Second Shift)

import os # Just to clear the garbage data in from the terminal
os.system("cls") # Just to clear the garbage data in from the terminal

num = 100
sum_list = [] # Initialising empty list

for i in range(1 + 1, num + 1, 2):   # Using for loop and taking a step of 2 for even numbers starting from 2 and ending at 101 so that 100 will be included.
    sum_list.append(i)  # Appending all even numbers from 1 to 100 in a list

print(f"Sum of all even numbers from 1 to 100 is:\t{sum(sum_list)}")    # Summing up the list and printing the output