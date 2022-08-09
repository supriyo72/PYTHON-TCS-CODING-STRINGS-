alpha= str(input("Enter the string: ")) 
for i in alpha:
      if i>="a" and i<="z" or i>="A" and i<="Z":
            freq= alpha.count(i) 
            print(str(i) + ": " + str(freq) + "," , end=" ")