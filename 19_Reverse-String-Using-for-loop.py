def reverse(s):
    r_string=""
    for i in s:
        r_string =  i + r_string
    print("resevrse string",r_string)

s = input("enter string:")
print("original string:",s)
reverse(s)

