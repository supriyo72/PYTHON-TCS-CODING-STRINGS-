alpha= str(input("Enter a string: "))
alpha.lower()
new= " "
for i in alpha:
      ascii=ord(i)
      if ascii == ord('z'):
            new= new + 'a'
      else:
            new= new + chr(ascii+1)
           
print(new)