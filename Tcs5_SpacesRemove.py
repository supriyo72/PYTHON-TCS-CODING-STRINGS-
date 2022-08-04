alpha= str(input("Enter a string: "))

Spaces= " "
res=""

for i in alpha:
    if i in Spaces:
         alpha= alpha.replace(i, "")
                
print(alpha) 
        
        
        
