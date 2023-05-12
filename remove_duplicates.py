def remove(dup):
    new_list=[]
    for n in dup:
        if n not in new_list:
            new_list.append(n)
    return new_list

a=input("Enter:")
print(remove(a))
