def has_duplicates(l):
    return len(l)!=len(set(l)) 
print(has_duplicates([1,2,3,4,5]))
print(has_duplicates([1,2,3,4,8,2,5,4]))
