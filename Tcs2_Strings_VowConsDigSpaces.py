alpha= str(input("Enter a string: "))

vow=0
cons=0
digit=0
spaces=0

alpha = alpha.lower()
for i in range(0,len(alpha)):
      if alpha[i]=="a" or alpha[i]=="e" or alpha[i]=="i" or alpha[i]=="o" or alpha[i]=="u":
           vow= vow + 1
      
      elif alpha[i]>= "a" and alpha[i]<= "z":
           cons=cons+1
        
      elif alpha[i]>= "0" and alpha[i]<= "9":
           digit=digit+1
        
      else:
           spaces=spaces+1
       
print("Vowels: ",vow)
print("Cons: ",cons)
print("Digit: ",digit)
print("Spaces: ",spaces)