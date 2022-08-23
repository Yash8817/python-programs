def check_number(no):
    num =no
    result = 0
    n = len(str(no))
    while (no!=0):
        digit = num%10
        result += digit ** n
        no = no // 10
    if num == result:
        print(num ,"is a armstrong number")
    else:
        print(num ,"is not a armstrong number")
def range_number(r):
    for i in range(r):
        num = i
        result = 0
        n = len(str(i))
        while (i!=0):
            digit = num%10
            result += digit ** n
            i = i // 10
        if num == result:
            print(num)

    
while True:
    print("|-------- armstrong number:")
    print("1.what is armstrong number ?")
    print("2.check number is armstrong or not")
    print("3.print in range ")
    print("4.exit")
    ch= int(input("Enter choiec:"))
    if ch == 1:
        print("The number of n digit which are equal to \n sum of nth power of its digit")
    elif ch == 2:
        n = int(input("enter number:"))
        check_number(n)
    elif ch == 3:
        n = int(input("enter range:"))
        range_number(n)
    elif ch == 4:
        break
    else :
        print("invalid choice")
        
        
    
    
