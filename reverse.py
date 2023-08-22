n = int(input("enter number"))
rev=int(0)
while(n>0):
    temp=n%10
    rev=int(rev*10)+temp
    n=n//10
print("reverse is ",rev)