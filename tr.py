def reverse(n):
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    return s
n = int(input())
ans=reverse(n)
sum=ans+n
ans1=reverse(sum)
if(sum==ans1):
    print(sum)
else:
    print("Not Pallindrome")