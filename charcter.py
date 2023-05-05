char=input("Enter any character:")
if char>='A' and char<="Z":
    print("Upper case")

elif char>='a' and char<='z':
    print("lowercase")
elif char>='1' and char<='9':
    print("digit")
else:
    print("special character")
