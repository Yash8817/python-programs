lower= int(input("enter lower interval:"))
upper= int(input("enter upper interval:"))

for num in range(lower,upper+1):
    res = 0
    for i in range(1,num):
        if num %i ==0:
            res += i
    if res == num:
        print(num)
    
