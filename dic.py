def dic(d):
    a={}
    for key,value in d.items():
        a[value]=key
    return a
d={}
no_of_items=int(input("Enter the no.of items in dictionary:"))
for i in range(no_of_items):
    key=input("Enter key:")
    value=input("enter value:")
    d[key]=value

a=dic(d)
print("Original dic:",d)
print("New dic:",a)
