alpha=  str(input("Enter a string: "))

vow=0
cons=0
alpha = alpha.lower()
for i in range(0,len(alpha)):
    # print(i)
    if alpha[i]=="a" or alpha[i]=="e" or alpha[i]=="i" or alpha[i]=="o" or alpha[i]=="u":
        vow= vow + 1

    elif alpha[i]!="a" or alpha[i]!="e" or alpha[i]!="i" or alpha[i]!="o" or alpha[i]!="u":
        cons=cons+1

print(vow)
print(cons)