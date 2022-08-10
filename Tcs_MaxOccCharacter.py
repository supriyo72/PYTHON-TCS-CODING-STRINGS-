alpha= str(input("Enter the string: "))
max=0

for i in alpha:
    cnt=alpha.count(i)
    if cnt>max :
        max= cnt
        maxA= i
print("Highest character is: ",maxA)

