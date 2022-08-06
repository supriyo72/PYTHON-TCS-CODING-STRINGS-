# alpha= str(input("Enter the string: "))

# count=0
# for i in range(0,len(alpha)):
#     for j in range(0,len(alpha)):
#         if alpha[i] == alpha[j]:
#             count=count+1
            





alpha= str(input("Enter the string: "))
alpha= alpha.lower()
for i in alpha:
    freq= alpha.count(i)
    
    if freq == 1 and i>="a" and i<="z":
        print(i, end=" ")
