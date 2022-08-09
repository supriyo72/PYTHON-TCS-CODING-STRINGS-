alpha= str(input("Enter the string: ")) 
res= [ ]
for i in alpha:
     dup= alpha.count(i)
     if dup > 1 and i>="a" and i<="z" or i>="A" and i<="Z":       
          if i not in res:
             res.append(i)
             result= " "
             d=result.join(res)
print(d)

          