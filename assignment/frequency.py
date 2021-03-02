userInput = eval(input("Enter a list [1,2,3,4,...]: "))
num = eval(input("Enter number to get frequency of: "))

count = 0

for item in userInput:
    if item == num:
        count +=1

print(f"Number To Find: {num}\t\tFound: {count} Times")