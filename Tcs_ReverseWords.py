str1= str(input("Enter a string1: "))
a= str1.split()
d=a[-1:-len(str1)-1:-1]
res1= " "
res= res1.join(d)
print(res)
