alpha= str(input("Enter the string: "))

for i in alpha:
    freq= alpha.count(i)
    
    if freq > 1:
        print(str(i) + " " + str(freq))
