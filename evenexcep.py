try:
  n=int(input("Enter num:"))
  if n%2==0:
    even=n
  print("Even num",even)
except:
  print("Odd num")
finally:
  print("Its a num")
