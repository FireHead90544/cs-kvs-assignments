names = eval(input("Enter A List ['name1', 'name2',...]: "))
count = 0
for name in names:
    if name.lower().startswith("a"):
        count += 1
print(count)