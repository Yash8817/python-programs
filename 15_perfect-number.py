n = int(input("enter value:"))
res = 0
for i in range(1,n):
    if n %i ==0:
        res += i
if res == n:
    print("perfect number:")
else:
    print("not a perfect number")
