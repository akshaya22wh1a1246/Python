def capitalize(s):
    words=s.split()
    new_sen=" "
    for word in words:
        new_word=word[0].upper()+word[1:].lower()
        new_sen+=new_word+" "
    return new_sen[:-1]
str1=input("Enter a sentence")
print(capitalize(str1))
