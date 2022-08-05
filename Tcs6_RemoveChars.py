n= str(input("Enter a string: "))

res=""
for i in range(0,len(n)):
    if n[i] >= "a" and n[i] <= "z" or n[i] >= "A" and n[i] <= "Z":
        res=res+n[i]
print(res)