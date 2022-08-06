alpha= str(input("Enter the string: "))

for i in alpha:
    freq= alpha.count(i)
    
    print(str(i) + ": " + str(freq))