def generate_binary(n):
    if n==0:
        return[' ']
    else:
        prev_str=generate_binary(n-1)
        new_str=[]
        for string in prev_str:
            new_str.append(string+'0')
            new_str.append(string+'1')
        return new_str

num=int(input("enter num:"))
print(generate_binary(num))
