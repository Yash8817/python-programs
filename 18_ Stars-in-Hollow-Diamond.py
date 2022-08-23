n= 5

for row in range(n):
    for col in range(n):
        if col+row == 2 or col-row==2 or row-col == 2 or row+col==6:
            print("*",end="")
        else:
            print(end=" ")
    print()
