f1=open("fir.txt","r")
f2=open("f2.txt","r")
a=""
for i in f1:
  a+=i
for j in f2:
  a+=j
f1.close()
f2.close()
f3=open("merge.txt","w")
f3.write(a)
f3.close()
f3=open("merge.txt","r")
print(f3.read())  
