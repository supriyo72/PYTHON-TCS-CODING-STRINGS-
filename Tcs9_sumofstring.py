n= str(input("Enter a string: "))

res= 0
for i in n:
    if i>= "0" and i <= "9":
        res=res+int(i)

print(res)