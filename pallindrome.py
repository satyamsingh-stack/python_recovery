n=int(input("Enter the Number:"))
s=0
k=n
while(n>0):
    r=n%10
    n=n//10
    s=s*10+r
print(s)
if(s==k):
    print("Pallindrome")
else:
    print("Not Pallindrome")