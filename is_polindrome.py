def is_polindrome(s,l):
    for i in range(0,l+1):
        if s[i]==s[l-1]:
            return True
        else:
            return False

string=input("Enter a string:")
length=len(string)
print(is_polindrome(string,length))

