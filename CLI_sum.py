import sys
n = len(sys.argv)
for i in range(1, n):
    print(sys.argv[i], end=" ")
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
print("Sum is :", sum)