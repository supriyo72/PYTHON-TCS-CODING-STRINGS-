# alpha= str(input("Enter a string: "))
# bracs= ("(" , ")")
# res=""
# for i in range(0,len(alpha)):
#      if alpha[i] not in bracs:
#              res=res+alpha[i]
# print(res)





alpha= str(input("Enter a string: "))
bracs= ("(" , ")")
res=""
for i in alpha:
    if i not in bracs:
        res=res+i
print(res)