alpha= str(input("Enter a string: "))

vow=("a","e","i","o","u")
res=""

for i in alpha:
      if i not in vow:
           res= res+i
print(res)