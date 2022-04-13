n=int(input("Enter a number:"))
tot=0
while(n>0)or(n<1000):
    dig=n%10
    tot=tot+dig
    n=n//10
else:
    print("Invalid")
print("The total sum of digits is:",tot)