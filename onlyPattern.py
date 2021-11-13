# n=4
# for r in range(1,n+1):
#     for c in range(1,n+1):
#         if(c>=1 and c<=r):
#             print("*",end=" ")
#     print()

n=5
for r in range(1,n+1):
    for c in range(1,n+1):
        if(c>=1 and c<=n-r):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


# n=4
# for r in range(1,n+1):
#     for c in range(1,n+1):
#         if(c>=1 and c<=n+1-r):
#             print("*",end=" ")
#     print()


# n=int(input())
# for r in range(1,n*3+3):
#     if(r%3==0):
#         print("*****")
#     else:
#         print("*   *")
# print()

#
# n=3
# for r in range(1,n+1):
#     for c in range(1,2*n):
#         if(c>=1 and c<=n-r):
#             print(" ",end=" ")
#         elif(c>=n-r+1 and c<=n+r-1):
#             print("*",end=" ")
#     print()


# n=4
# for r in range(1,n+1):
#     for c in range(1,2*n):
#         if(c<=n+r-1 and c>=n-r+1):
#             print("*",end=" ")
#         elif(c>=1 and c<=n-r and c<=2*n and c>=n-r+2):
#             print(" ",end=" ")
#     print()



# n=5
# for r in range(1,n+1):
#     for c in range(1,n+1):
#         if(c>=1 and c<=n-r):
#             print(" ",end=" ")
#         else:
#             print(" * ",end=" ")
#     print()