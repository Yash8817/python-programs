s1 = input("enter string:")
s2 = input("enter string:")

if len(s1)==len(s2):
    if sorted(s1)==sorted(s2):
        print("string is anagram")
    else:
        print("string is not anagram")
else:
    print("string is not anagram")
