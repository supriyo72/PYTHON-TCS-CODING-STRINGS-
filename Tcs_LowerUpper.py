word= str(input("Enter a word: "))

temp=""
for i in word:
    if i>="a" and i<="z":
        res1= i.upper()
        # print(res1,end=" ")
        temp=temp+res1
                
    elif i>="A" and i<="Z":
        res2= i.lower()
        # print(res2,end=" ")
        temp=temp+res2
print(temp)