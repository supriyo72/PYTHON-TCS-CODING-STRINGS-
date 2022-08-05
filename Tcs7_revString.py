# str= str(input("Enter a string: "))
# d=str[-1:-len(str)-1:-1]

# print(d)

str= str(input("Enter a string: "))

def revString(str):
    reverse= str[::-1]
    return reverse

a= revString(str)
print(a)