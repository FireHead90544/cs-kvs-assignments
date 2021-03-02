userInput = eval(input("Enter A List ['elem1', 'elem2', 3, 4,...]: "))

uniqueness = {}

for item in userInput:
    if item in uniqueness.keys():
        uniqueness[item] = uniqueness[item] + 1
    else:
        uniqueness[item] = 1 

for item in uniqueness.keys():
    if uniqueness[item] == 1:
        print(f"{item} - Unique (1 Time)")
    else:
        print(f"{item} - Duplicate ({uniqueness[item]} Times)")



'''
# Another Approach: Using collections.Counter(), uncomment to use :)
import collections
userInput = eval(input("Enter A List ['elem1', 'elem2', 3, 4,...]: "))
counter = collections.Counter(userInput)
for item in counter.keys():
    if counter[item] == 1:
        print(f"{item} - Unique (1 Time)")
    else:
        print(f"{item} - Duplicate ({counter[item]} Times)")
'''