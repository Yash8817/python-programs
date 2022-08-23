def findGCD(a,b):
    if b == 0:
        return a
    else:
        return findGCD(b,a%b)
    
a = int(input("enter a value:"))
b = int(input("enter b value:"))
print(findGCD(a,b))
