str1= str(input("Enter a string1: "))
str2= str(input("Enter a string2: "))

a= str1.split()
b= str2.split()

c=[]
for i in a:
    if i in b:
        c.append(i)
        
print(c)