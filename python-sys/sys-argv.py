import sys
n = len(sys.argv)

print("Total arguments passed:", n)
print("Name of Python script:", sys.argv[0])
print("Arguments passed:", end=" ")

for i in range(1, n):
    print(sys.argv[i], end=" ")
print("\n")

Sum = 0
for i in range(1, n):
    Sum += int(sys.argv[i])

print(Sum)