import math
n1 = int(input("enter string:"))
n2= int(input("enter string:"))

if math.gcd(n1,n2) == 1:
    print("numbers are co-prime")
else:
    print("numbers are not co-prime")


