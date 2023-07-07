def OR(n1,n2):
  return n1|n2
def AND(n1,n2):
  return n1&n2
def NOT(n1):
  return ~n1+2
def XOR(n1,n2):
  return n1^n2

a=int(input("Enter n1:"))
b=int(input("Ente n2:"))
print(OR(a,b))
print(AND(a,b))
print(NOT(a))
print(XOR(a,b))
