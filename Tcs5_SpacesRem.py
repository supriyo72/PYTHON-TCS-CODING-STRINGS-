alpha= str(input("Enter a string: "))

Spaces= " "
res=""

for i in range(0,len(alpha)):
     if alpha[i] not in Spaces:
             res=res+alpha[i]
            
print(res)         
        
        
