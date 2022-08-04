alpha= str(input("Enter a string: "))

vow=("a","e","i","o","u")
res=""

for i in range(0,len(alpha)):
      if alpha[i] not in vow:
          res= res+ alpha[i]
print(res)      