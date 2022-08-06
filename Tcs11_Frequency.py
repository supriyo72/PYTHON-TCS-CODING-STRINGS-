# alpha= str(input("Enter the string: "))
# find=str(input("Which string to find: "))

# count=0
# for i in alpha:
#     if i in find:
#         count=count+1
        
# print(count)




alpha= str(input("Enter the string: "))
find=str(input("Which string to find: "))

count=0
i=0
while(i<len(alpha)):
    if alpha[i]==find:
        count=count+1
        
        
    i+=1
    
print(count)