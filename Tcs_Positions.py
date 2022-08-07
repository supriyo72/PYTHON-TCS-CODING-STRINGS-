word= str(input("Enter a word: "))
fnd=str(input("What to find: "))

if word.find(fnd) != -1:
    print("It contains given substring")
else:
    print("It does'nt contain any substring")
result= word.find(fnd)
print(result)