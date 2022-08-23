n=int(input("Enter number:"))

if n > 1:
    for num in range(2,n):
        if n % num == 0:
            print("not a prime number")
            break
    else:
        print("prime number")
            
