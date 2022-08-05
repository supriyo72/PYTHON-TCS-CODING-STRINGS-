alpha= str(input("Enter a string: "))
s=alpha.title()
word= s.split()

string= ""

for i in word:
     string+= i[:-1]+i[-1].upper()+ " "

print(string)
