string= input("Enter number:")

n = len(string)
for i in range(n):
    for j in range(i+1):
        print(string[j] , end=" ")
    else:
        print(end=" ")
    print()
