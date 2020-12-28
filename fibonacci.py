# Program to display the Fibonacci sequence up to 10 terms
# Programmed by Rudransh Joshi
# Class: XI - A (Second Shift)

import os # Just to clear the garbage data in from the terminal
os.system("cls") # Just to clear the garbage data in from the terminal

nterms = 10 # First ten terms

# First two terms
n1, n2 = 0, 1
count = 0

fibo_int = []  # As numbers will be stored in int here

print("Fibonacci Series Upto 10 Terms:", end="\t\t")
while count < nterms:
   fibo_int.append(n1)
   nth = n1 + n2
   # update values
   n1 = n2
   n2 = nth
   count += 1

fibonacci_series = []  # Converting int to str because `"".join()` uses str instead of int

for item in fibo_int:
   item = str(item)
   fibonacci_series.append(item)

print(", ".join(fibonacci_series))