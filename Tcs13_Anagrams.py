alpha1= str(input("Enter a string1: "))
alpha2= str(input("Enter a string2: "))

count=0
for i in alpha1:
    if i in alpha2:
        count=count+1
        
if count==len(alpha2):
    print("Anagram")
else:
    print("Not Anagram")