str= str(input("Enter a string: "))
d=str[-1:-len(str)-1:-1]


if(str[0:len(str)] == d):
    print("Pallindrome")
else:
    print("Not pallindrome")