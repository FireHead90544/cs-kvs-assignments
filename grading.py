# Program to award grades to students using below grading system
'''
MARKS              |  GRADE
-------------------|------------
>=91               |    A
<=90 AND >=81      |    B
<=80 AND >=71      |    C
<=70               |    D
'''
# Programmed by Rudransh Joshi
# Class: XI - A (Second Shift)

import os # Just to clear the garbage data in from the terminal
os.system("cls") # Just to clear the garbage data in from the terminal


def calculateMarks(marks):
    if marks >= 91:
        print(f"A! You got grade A.\n")
    elif marks <= 90 and marks >=81:
        print(f"B! You got grade B.\n")
    elif marks <= 80 and marks >= 71:
        print(f"C! You got grade C.\n")    
    elif marks <= 70:
        print(f"D! You got grade D.\n")
    else:
        print(f"Invalid Marks!")

while True:
    marks = int(input("Enter The Marks:\t"))
    calculateMarks(marks)        