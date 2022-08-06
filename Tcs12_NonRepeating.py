alpha= str(input("Enter the string: "))
alpha= alpha.lower()
for i in alpha:
    freq= alpha.count(i)
    
    if freq == 1 and i>="a" and i<="z":
        print(i, end=" ")
