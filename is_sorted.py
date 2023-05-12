def is_sorted(list1):
    list2=sorted(list1)
    if (list1==list2):
        return True
    else:
        return False

list1=input("Enter a list:")
list1=list1.split()
print(is_sorted(list1))
