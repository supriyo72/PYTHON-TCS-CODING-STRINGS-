alpha= str(input("Enter a string: "))

vow=("a","e","i","o","u")

alpha = alpha.lower()
for i in alpha:
      if i in vow:
          alpha= alpha.replace(i, "")
print(alpha)
        
 