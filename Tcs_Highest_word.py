alpha= str(input("Enter the string: "))
alpha=alpha.split()

max=0

for i in alpha:
      if len(i)>max:
             max= len(i)
             max_word=i
print("Highest word is: ", max_word)
            
              
          
